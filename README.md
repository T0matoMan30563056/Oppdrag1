#Nettverk Og Internett

Første Oppgaven var å sette på en statisk IP adresse og pinge mellom vår pi og laptopen vår. Jeg fikk IP adressen 10.200.14.25 og fikk endret det ganske lett ved å gå innit settings på nettverket
##Manuel Internett


Her måtte jeg bytte det fra Automatic (DHCP) til Manuel. Her endret jeg adressen, nettmasken og defult gatewayen.

##kjekke ip etter jeg forandret den
 
Etter jeg bytta det og lagret gikk jeg inni terminalen og ved å bruke «ip a» fikk jeg vite at min IP adresset ble byttet til 10.200.14.25
##Internett før jeg forandra på den

her er hvordan din adresse ser ut med Automatisk IP adresse

##Pinge Pi fra Laptop
 
Etter at jeg fikk endre IP, gikk jeg på min laptop og pingte IP adressen min. Dette lykkes og vi kan se at jeg fikk til å andre adressen
#Server Og Tjeneser
I denne oppgaven skulle vi enten sette opp en python http-server ved å bruke python3 eller å sette en apache server. Jeg valgte å gå med en python http-server

##Sette Opp Python3 server (http.server)
 
Her fikk jeg till å navigere fill systemet i terminalen for å bryke «python3 -m http.server 8000» i min screenshots mappa so jeg kunne dele bildene på serverene for å finne nettsiden måtte du skrive ip adressen 10.200.14.25:8000
 

Dette er hvordan nettsiden så ut. Uten denne «:8000» ville jeg ha fått bare
 
Som er den default pagen for apache som jeg også fikk lastet ned. Jeg fikk lastet ned apache fra terminalen ved brukk av «sudo apt install apache2», men jeg fikk ikke bruke det fordi jeg valgte python http.server.
 
Etter jeg installerte apache sjekka jeg statusen, apache serveren automatisk skrur jeg på etter at den har blitt instalert. Etter serveren min har gått på spørte jeg omar om å koble seg på den, da så jeg at
 
Dette viser aktiviteten på serveren.

#Python og GitHub
Etter dette hadde jeg som oppgave å lage en python skript, dele den på github fra laptopen, og lastet det ned på pien. Jeg måtte laste ned git først
 

Jeg lagdte en basic code som sa hei 2IMI. 
Her måtte jeg logge inn og lage en ny repository, etter jeg lagde den satt inn hello.py inni denne. Ved å installere git fikk jeg tilgang til «git clone» som kloner eller installerer denne git coden
Jeg måtte laste ned denne code for å klone den til min system. Hvis jeg ville oppdatere den mappa jeg tok det fra kunne jeg bruke git pull også denne coden igjen. Det har ver en lett, men langtsom måte å dele filer på og jeg synes at samba var mye bedre










Her er coden som blir kjørt, jeg må først finne mappen ved bruk av cd og ls, cd er for å navigere, og ls for å see alle mulige mapper jeg kan gå inn. 

#Samba Extra Oppgave:
Alt startet med at jeg kjørte «sudo apt install samba» for å installere samba etter dette lagde jeg en mappe i min root ved bruk av
Sudo mkdir /sambashare

Jeg bruker mkdir for å lage en mappe, og ved å skrive / foran sambashare betyr det at den blir laget i root. Etter jeg lagde mappen i root ga jeg alle tilatelse til den ved bruk av 
Sudo chmod 777 /sambashare
Dette sier at jeg gir max tilatelse for alle som kommer inni mappen

For å add en user og password for mappen bruker jeg «sudo useradd smbusr» smbur er forkortelse for sambauser og jeg referere til den senere med bruk av 
«sudo smbpasswd -a smbusr» for å sette en ny password for brukeren, da var alt satt opp og jeg fikk til å dele mapper.
