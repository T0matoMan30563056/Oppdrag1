   #Nettverk Og Internett

Første Oppgaven var å sette på en statisk IP adresse og pinge mellom vår pi og laptopen vår. Jeg fikk IP adressen 10.200.14.25 og fikk endret det ganske lett ved å gå innit settings på nettverket
- Manuel Internett

<img width="850" height="700" alt="image" src="https://github.com/user-attachments/assets/9b23095b-cd9d-443b-bf83-27411e73a998" />

Her måtte jeg bytte det fra Automatic (DHCP) til Manuel. Her endret jeg adressen, nettmasken og defult gatewayen.
- kjekke ip etter jeg forandret den

<img width="945" height="339" alt="image" src="https://github.com/user-attachments/assets/0e5b2b2b-5814-4049-8ec0-4ff4d6e20707" /> 

Etter jeg bytta det og lagret gikk jeg inni terminalen og ved å bruke «ip a» fikk jeg vite at min IP adresset ble byttet til 10.200.14.25
- Internett før jeg forandra på den

<img width="850" height="324" alt="image" src="https://github.com/user-attachments/assets/9b654e63-662d-45ec-8ce0-d501af8968c7" />

her er hvordan din adresse ser ut med Automatisk IP adresse
- Pinge Pi fra Laptop

<img width="945" height="430" alt="image" src="https://github.com/user-attachments/assets/01d8e4ea-8776-4347-9074-e487cf02fb97" />

Etter at jeg fikk endre IP, gikk jeg på min laptop og pingte IP adressen min. Dette lykkes og vi kan se at jeg fikk til å andre adressen
  
   
   #Server Og Tjeneser
   
I denne oppgaven skulle vi enten sette opp en python http-server ved å bruke python3 eller å sette en apache server. Jeg valgte å gå med en python http-server

- Sette Opp Python3 server (http.server)

<img width="945" height="671" alt="image" src="https://github.com/user-attachments/assets/7966a79b-4fdd-4cb7-a7e3-782be80fe0c4" />

Her fikk jeg till å navigere fill systemet i terminalen for å bryke «python3 -m http.server 8000» i min screenshots mappa so jeg kunne dele bildene på serverene for å finne nettsiden måtte du skrive ip adressen 10.200.14.25:8000
Dette er hvordan nettsiden så ut. Uten denne «:8000» ville jeg ha fått bare

- Defult Apache

<img width="945" height="590" alt="image" src="https://github.com/user-attachments/assets/a050a8ef-9d07-42a8-9e91-3ccc7a541332" /> 

Som er den default pagen for apache som jeg også fikk lastet ned. Jeg fikk lastet ned apache fra terminalen ved brukk av «sudo apt install apache2», men jeg fikk ikke bruke det fordi jeg valgte python http.server.

- python nettside

<img width="945" height="207" alt="image" src="https://github.com/user-attachments/assets/69859998-09a4-427b-8d33-b5eaf85ff05c" />

Etter jeg installerte apache sjekka jeg statusen, apache serveren automatisk skrur jeg på etter at den har blitt instalert. Etter serveren min har gått på spørte jeg omar om å koble seg på den, da så jeg at

- aktivitet fra python3 serveren
<img width="696" height="96" alt="image" src="https://github.com/user-attachments/assets/7e287f38-942c-4b9f-b4e2-72d172adac65" />

Dette viser aktiviteten på serveren.



   #Python og GitHub

   
Etter dette hadde jeg som oppgave å lage en python skript, dele den på github fra laptopen, og lastet det ned på pien. Jeg måtte laste ned git først

- Nedlasting av Git

<img width="945" height="703" alt="image" src="https://github.com/user-attachments/assets/21c14ff7-52bd-4219-9e38-6f6d917ac931" />

Jeg lagdte en basic code som sa hei 2IMI.

- Img av GItHub Side

<img width="945" height="590" alt="image" src="https://github.com/user-attachments/assets/cd2cedc1-ed05-4e8f-8728-69c59bf97213" />

Her måtte jeg logge inn og lage en ny repository, etter jeg lagde den satt inn hello.py inni denne. Ved å installere git fikk jeg tilgang til «git clone» som kloner eller installerer denne git coden
Jeg måtte laste ned denne code for å klone den til min system. Hvis jeg ville oppdatere den mappa jeg tok det fra kunne jeg bruke git pull også denne coden igjen. Det har ver en lett, men langtsom måte å dele filer på og jeg synes at samba var mye bedre
- clone på github 

<img width="571" height="425" alt="image" src="https://github.com/user-attachments/assets/9b2d988c-b996-48ab-aa3a-ad7548a6b631" />

Her er coden som blir kjørt, jeg må først finne mappen ved bruk av cd og ls, cd er for å navigere, og ls for å see alle mulige mapper jeg kan gå inn. 

<img width="944" height="413" alt="image" src="https://github.com/user-attachments/assets/0a90ecbb-c552-4477-86b8-6f96e7bf86fa" />

   #Samba Extra Oppgave:
   
Alt startet med at jeg kjørte «sudo apt install samba» for å installere samba etter dette lagde jeg en mappe i min root ved bruk av
Sudo mkdir /sambashare

Jeg bruker mkdir for å lage en mappe, og ved å skrive / foran sambashare betyr det at den blir laget i root. Etter jeg lagde mappen i root ga jeg alle tilatelse til den ved bruk av 
Sudo chmod 777 /sambashare
Dette sier at jeg gir max tilatelse for alle som kommer inni mappen

For å add en user og password for mappen bruker jeg «sudo useradd smbusr» smbur er forkortelse for sambauser og jeg referere til den senere med bruk av 
«sudo smbpasswd -a smbusr» for å sette en ny password for brukeren, da var alt satt opp og jeg fikk til å dele mapper.
- hvordan Sambamappen så ut etter fulle satt opp og testa

<img width="1919" height="1199" alt="Skjermbilde 2025-09-17 115324" src="https://github.com/user-attachments/assets/e03f2f68-019e-4340-8f8a-cd7eab6c1530" />

