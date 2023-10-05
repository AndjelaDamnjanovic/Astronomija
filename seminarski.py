import sys
import math
import time

# fja koja u slucaju greske ispisuje odgovarajucu poruku i nakon 5 sekundi prekida izvrsavanje programa
def error(msg):
    print('\n');
    print(msg);
    time.sleep(5);
    sys.exit();

#fja koja konvertuje stepene u sate
def degToHour(deg):
    return deg/15.0;

#fja koja prevodi iz oblika HH MM SS u H u decimalnom zapisu
def HMStoH(h,m,s):
    return ((s/60)+m)/60+h;

#fja koja ispisuje krajnji rezultat
def write(deg):
    d=int(deg);
    m=int((deg-d)*60);
    s=round(((deg-d)*60-m)*60,2);
    d=str(d);
    m=str(m);
    s=str(s);
    msg="Vreme je: "+d+"h "+m+"min "+s+"sec";
    print('\n');
    print(msg);

#fja za konverziju srednjeg vremena u zvezdano
def sredUzvezd(S0, longitude, ts):
    S0=float(S0);
    longitude=float(longitude);
    ts=float(ts);
    rez=S0-longitude*(1/365.2422)+ts*(1+1/365.2422);
    if rez>24:
        rez=rez-24;
    if rez<0:
        rez=rez+24;
    write(rez);

#fja za konverziju zvezdanog vremena u srednje vreme
def zvezdUsred(s, S0, longitude):
    s=float(s);
    S0=float(S0);
    longitude=float(longitude);
    ts=(s-S0+longitude*(1/365.2422))*(1-1/366.2422);
    if ts>24:
        ts=ts-24;
    if ts<0:
        ts=ts+24;
    write(ts);

#fja konvertuje zonsko u srednje vreme
def zoneToUT(zon, longitude):
    zon=float(zon);
    longitude=float(longitude);
    Ts=zon-int(longitude);
    ts=Ts+longitude;
    if ts>24:
        ts=ts-24;
    if ts<0:
        ts=ts+24;
    write(ts);

#fja koja konvertuje srednje vreme u zonsko vreme u zoni po izboru korisnika
def UTtoZone(ts, longitude, zone):
    ts=float(ts);
    longitude=float(longitude);
    zone=int(zone);
    Ts=ts-longitude;
    zon=Ts+zone;
    if zon>24:
        zon=zon-24;
    if zon<0:
        zon=zon+24;
    write(zon);

#fja koja konvertuje zonsko vreme u zvezdano
def zoneTozvezd(S0, zon, longitude):
    S0=float(S0);
    zon=float(zon);
    longitude=float(longitude);
    Ts=zon-int(longitude);
    ts=Ts+longitude;
    if ts>24:
        ts=ts-24;
    if ts<0:
        ts=ts+24;
    sredUzvezd(S0, longitude, ts);

#fja koja konvertuje zvezdano u zonsko vreme u zoni po izboru korisnika
def zvezdTozone(s, S0, longitude, zone):
    s=float(s);
    S0=float(S0);
    longitude=float(longitude);
    zone=int(zone);
    ts=(s-S0+longitude*(1/365.2422))*(1-1/366.2422);
    if ts>24:
        ts=ts-24;
    if ts<0:
        ts=ts+24;
    UTtoZone(ts, longitude, zone);

#korisnik zadaje vremenski sistem u koji zeli da konvertuje vreme i onaj iz kog zeli da konvertuje vreme
inp=int(input("Upisite redni broj sistema vremena iz kojeg biste zeleli da konvertujete (1 za zvezdano, 2 za srednje ili 3 za zonsko):")); 
if inp>3 or inp<1:
    error("Greska! Morate uneti 1, 2 ili 3!!!");

out=int(input("Upisite redni broj sistema vremena u koji biste zeleli da konvertujete (1 za zvezdano, 2 za srednje ili 3 za zonsko):"));
if out<1 or out>3:
    error("Greska! Morate unesti broj 1, 2 ili 3!!!");

if inp==out:
    error("Greska! Da biste uspesno konvertovali ulazni i izlazni indeksi moraju biti razliciti!!!");

#unos geografske duzine je razmatran posebno, jer je potreban pri svakoj konverziji, korisnik bira da li ce uneti vreme u satima ili stepenima
long=int(input("Unesite indikator za geografsku duzinu (1 ako zelite da unesete stepene ili 2 ako zelite da unesete sate):"));
if long!=1 and long!=2:
    error("Greska! Morate uneti ili 1 ili 2!!!");

if long==2:
    lh, lm, ls= input("Unesite sate (u intervalu od -12 do 12), minute (celobrojna vrednost) i sekunde (realna vrednost) za duzinu:").split();
    lh=int(lh);
    lm=int(lm);
    ls=float(ls);
    if lm>=60 or lm<0 or ls>=60 or ls<0 or lh>12 or lh<(-12):
        error("Greska! Minuti i sekunde moraju biti u opsegu od 0 do 60, a sati u rasponu od -12 do 12!!!");
    l=HMStoH(lh, lm, ls);

if long==1:
    lh, lm, ls= input("Unesite stepene (u intervalu -180 do 180), minute (celobrojna vrednost) i sekunde (realna vrednost) za duzinu:").split();
    lh=int(lh);
    lm=int(lm);
    ls=float(ls);
    if lm>=60 or lm<0 or ls>=60 or ls<0 or lh>180 or lh<(-180):
        error("Greska! Minuti i sekunde moraju biti u opsegu od 0 do 60, a stepeni u rasponu od -180 do 180!!!");
    l=HMStoH(lh, lm, ls);
    l=degToHour(l);

#konverzija iz zvezdanog vremena
if inp==1:
    sh, sm, ss= input("Unesite sate (celobrojna vrednost), minute (celobrojna vrednost) i sekunde (realna vrednost) zvezdanog vremena:").split();
    sh=int(sh);
    sm=int(sm);
    ss=float(ss);
    if sm>=60 or sm<0 or ss>=60 or ss<0 or sh>=24 or sh<0:
        error("Greska! Minuti i sekunde moraju biti u opsegu od 0 do 60, a sati u rasponu od 0 do 24!!!");
    s=HMStoH(sh, sm, ss);
    Sh, Sm, Ss= input("Unesite sate (celobrojna vrednost), minute (celobrojna vrednost) i sekunde (realna vrednost) za S0:").split();
    Sh=int(Sh);
    Sm=int(Sm);
    Ss=float(Ss);
    if Sm>=60 or Sm<0 or Ss>=60 or Ss<0 or Sh>=24 or Sh<0:
        error("Greska! Minuti i sekunde moraju biti u opsegu od 0 do 60, a sati u rasponu od 0 do 24!!!");
    S0=HMStoH(Sh, Sm, Ss);
    if out==2:
        zvezdUsred(s, S0, l);
    if out==3:
        z=int(input("Unesite redni broj zone u koju zelite da konvertujete vreme:"));
        if z<0 or z>=24:
            error("Greska! Redni broj zone mora biti broj izmedju 0 i 24!!!");
        zvezdTozone(s, S0, l, z);

#konverzija iz srednjeg vremena
if inp==2:
    th, tm, tse= input("Unesite sate (celobrojna vrednost), minute (celobrojna vrednost) i sekunde (realna vrednost) srednjeg vremena:").split();
    th=int(th);
    tm=int(tm);
    tse=float(tse);
    if tm>=60 or tm<0 or tse>=60 or tse<0 or th>=24 or th<0:
        error("Greska! Minuti i sekunde moraju biti u opsegu od 0 do 60, a sati u rasponu od 0 do 24!!!");
    ts=HMStoH(th, tm, tse);
    if out==1:
        Sh, Sm, Ss= input("Unesite sate (celobrojna vrednost), minute (celobrojna vrednost) i sekunde (realna vrednost) za S0:").split();
        Sh=int(Sh);
        Sm=int(Sm);
        Ss=float(Ss);
        if Sm>=60 or Sm<0 or Ss>=60 or Ss<0 or Sh>=24 or Sh<0:
            error("Greska! Minuti i sekunde moraju biti u opsegu od 0 do 60, a sati u rasponu od 0 do 24!!!");
        S0=HMStoH(Sh, Sm, Ss);
        sredUzvezd(S0, l, ts);
    if out==3:
        z=int(input("Unesite redni broj zone u koju zelite da konvertujete vreme:"));
        if z<0 or z>=24:
            error("Greska! Redni broj zone mora biti broj izmedju 0 i 24!!!");
        UTtoZone(ts, l, z);

#konverzije iz zonskog vremena
if inp==3:
    zh, zm, zs= input("Unesite sate (celobrojna vrednost), minute (celobrojna vrednost) i sekunde (realna vrednost) zonskog vremena:").split();
    zh=int(zh);
    zm=int(zm);
    zs=float(zs);
    if zm>=60 or zm<0 or zs>=60 or zs<0 or zh>=24 or zh<0:
        error("Greska! Minuti i sekunde moraju biti u opsegu od 0 do 60, a sati u rasponu od 0 do 24!!!");
    z=HMStoH(zh, zm, zs);
    if out==2:
        zoneToUT(z, l);
    if out==1:
        Sh, Sm, Ss= input("Unesite sate (celobrojna vrednost), minute (celobrojna vrednost) i sekunde (realna vrednost) za S0:").split();
        Sh=int(Sh);
        Sm=int(Sm);
        Ss=float(Ss);
        if Sm>=60 or Sm<0 or Ss>=60 or Ss<0 or Sh>=24 or Sh<0:
            error("Greska! Minuti i sekunde moraju biti u opsegu od 0 do 60, a sati u rasponu od 0 do 24!!!");
        S0=HMStoH(Sh, Sm, Ss);
        zoneTozvezd(S0, z, l);

