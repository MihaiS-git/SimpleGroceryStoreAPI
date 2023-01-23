# SimpleGroceryStoreAPI
QA Automation Project - API Tests

In prezentul proiect, am realizat testarea automata a unui API, specific unei pagini web de ecommerce. 
API-ul testat se numeste Simple Grocery Store API, are URL-ul de baza
https://simple-grocery-store-api.glitch.me, iar documentatia completa a acestuia poate fi gasita
pe Github https://www.postman.com/brooks81/workspace/rest-api-testing/documentation/21662525-4dcfdced-35c1-44c8-97b9-c4a04a0f159b

Proiectul contine 44 de teste, din care 4 teste cad din cauza unor bug-uri descoperite in API.
Bug-urile constau in dublarea id-ului unor produse si in returnarea de produse diferite in cazul
request-ului pe categorii de produse fata de request-ul de returnare a intregii liste de produse.

Simple Grocery Store API are un numar de 5 endpoint-uri, ‘Status’, ‘Products’, ‘Cart’, ‘Orders’
si ‘API Authentication’ care au fost testate fiecare in parte. Pentru scrierea testelor, am folosit
limbajul de programare ‘Python 3.10.5’ si IDE-ul ‘PyCharm’. Am utilizat, de asemenea,
framework-ul ‘Pytest’ care faciliteaza scrierea de teste automate si rularea acestora atat in
pachet, cat si in mod independent, libraria ‘pytest-html’ pentru generarea raportului in format
html, libraria ‘requests’ pentru trimiterea request-urilor catre API, ‘json’ si ‘jsonschema‘ pentru
raspunsurile de tip JSON primite de la API, respectiv librarira ‘assertpy’ pentru validarea
testelor

Testarea automata realizata este o testare de tip black-box, functionalitatea si securitatea API-ul au
fost testate fara a avea access nici la cod, nici la structura interna a acestuia. Testarea de tip
black-box a fost realizata cu focusare pe inputs si outputs:

- Examinarea documentatiei si testarea manuala a functionalitatii API-ului cu Postman,
stabilind input-uri valide pentru requests si obtinand raspunsuri de tip JSON, respectiv
HTTP code response-urile aferente
- Positiv test scenario & negativ test scenario – scrierea in Python de teste cu input-uri
valide si scrierea de teste cu input-uri invalide pentru verificarea functionarii corecte
- Validarea raspunsurilor primite in functie de input-uri si raspunsurile asteptate, respectiv
‘schema’ JSON a raspunsurilor
- Construirea de scenarii de testare pe baza input-urilor testate anterior
- Executarea test case-urilor
- Compararea raspunsurilor primite cu raspunsurile asteptate
- Verificarea securitatii prin testarea validitatii structurii raspunsurilor
- Verificarea securitatii testand folosirea de input-uri de autentificare invalide

Proiectul poate fi clonat si rulat astfel:

Prerequisites:
- instalare Python https://www.python.org/downloads/
- instalare IDE https://www.jetbrains.com/pycharm/download
- instalare Git https://gitforwindows.org
- 
Rulare teste:
- se creeaza un folder local pentru clonarea proiectului
- se deschide Git Bash din folderul creat
- se utilizeaza in Git Bash comanda: git clone https://github.com/MihaiS-git/SimpleGroceryStoreAPI
- se deschide IDE-ul instalat, iar din terminal se acceseaza adresa folderului in care a fost clonat
proiectul
- tot din terminalul IDE-ului, se vor instala toate pachetele necesare specificate in fisierul
‘requirements.txt’, folosind comanda: pip install -r requirements.txt
- din terminalul IDE-ului, din folderul ‘tests’, pentru rularea testelor si generarea raportului
html, se utlizeaza comanda: pytest --html=report.html --self-contained-html
- raportul html generat poate fi gasit in folderul ‘tests/report.html’


Proiectul a fost structurat in mai multe foldere, fiecare avand un rol distinct in asamblul si 
functionalitatea proiectului, astfel:

- api_requests – contine fisierul ‘api_requests.py’ unde sunt toate functiile pentru timiterea de 
request-uri catre API, folosind principalele metode HTTP: GET, POST, PUT,
PATCH, DELETE
- api_utils – contine fisierul ‘api_utils.py’ unde este stocat URL-ul de baza pentru apelarea 
API-ului, parametri de apelare, functii de utilitate generala in cadrul proiectului, 
care genereaza, citesc si returneaza date de autentificare ale clientului, stocate in 
fisiere txt din acelasi folder
- json_schema – contine JSON ‘schema’ de validare pentru raspunsurile returnate de catre API
- tests – contine fisierele cu scenariile de test si raportul html generat in urma rularii testelor 
- validators – contine fisierul ‘json_validator.py’ cu functii de validare a JSON ‘schema’, 
utilizate in teste
 

Modul de accesare a endpoint-urilor API-ului – Exemple:

- Accesarea endpoint-ului ‘Status’ se poate face direct din browser cu URL-ul de baza la care se
adauga numele endpointului:
    https://simple-grocery-store-api.glitch.me/status
- Accesarea endpoint-ului ‘Products’:
    https://simple-grocery-store-api.glitch.me/products

Raspunsurile sunt in format JSON(JavaScript Object Notation). JSON este un format
realtiv simplu de gazduire si transmitere de date constituit din perechi ‘cheie’: ‘valoare’, usor
lizibil. Tipurile de date de baza ale JSON sunt: numeric, string, Boolean, array, object si null.
Pentru fiecare raspuns API in format JSON, se asteapta o anumita ‘schema’ pentru formatul datelor
returnate, care trebuie de asemenea validata, procesul facand parte din testarea de securitate.
Structurile ‘schema’ validate in prezentul proiect, pot fi accesate in folder-ul ‘json_schema’.

In fisierul ‘json_validator.py’ din folder-ul ‘validators’, am creat functia ‘validate_json_schema’ care 
realizeaza efectiv validarea, iar functia este apelata in toate metodele de validare, evitand astfel rescrierea 
codului. Parametrii functiei sunt raspunsul API-ului in format JSON si ‘schema’ ca format asteptat pentru 
structura raspunsului primit, citita dintr-un fisier text. Functia returneaza True sau False in urma validarii


Testarea functionalitatii API-ului:

test_api_functionality.py – contine toate teste de functionalitate a API-ului, scrise pe baza documentatiei
acestuia. Am creat o clasa de teste denumita ‘TestAPIFunctionality’. In primele linii, se regasesc cu
decoratorul ‘@pytest.fixture’, functii ce stabilesc baseline-ul pentru anumite teste din fisier. Practic, sunt
folosite ca si parametrii de intrare, stabilind un anumit mediu de lucru(environment) pentru teste sau alte
fixtures. De exemplu, creaza un cos de cumparaturi ‘cart_1_id’ si returneaza id-ul acestuia, folosit ulterior ca
si parametru atat intr-un alt fixture, cat si in testul ‘test_create_new_order’.
Urmeaza efectiv testele in sine, sub forma de metode ale caror nume incepe intotdeauna cu ‘test’, conform
instructiunilor PyTest. Astfel, aceste metode sunt recunoscute in mod automat ca si teste ce pot fi rulate si in
mod independent.
Pentru a asigura validitatea generala a testelor, la alegerea produselor returnate de API, am folosit modulul
in-built Python denumit ‘random’, care are utilitatea de a genera numere aleatorii dintr-un interval specificat sau
de a face alegeri aleatorii dintr-o lista.

Raportul HTML pentru ‘test_api_functionality.py’ ne arata ca testele au trecut cu o exceptie. Testul care solicita 
returnarea produselor de tip “bread-bakery, care a picat din cauza faptul ca solicitand lista 
tuturor produselor din API am obtinut 1 produs din acest tip si ne asteptam ca raspunsul sa fie acelasi si la 
request-ul pe categorie, insa sunt returnate 5 produse diferite.


Testarea securitatii API-ului:

test_api_security.py – contine teste de autentificare de tip negativ. Se testeaza inregistrarea unui nou client avand 
un nume deja utilizat, ceea ce este posibil, status code-ul asteptat fiind ‘201’ created, inregistrarea unui nou 
client cu un email deja utilizat, ceea ce nu este acceptat, status code-ul asteptat fiind ‘409’ request invalid. De 
asemenea se testeaza crearea unei noi comenzi(‘order’) cu un token de access fals, obtinerea tuturor sau a unei 
singure comenzi, repectiv stergerea unei comenzi cu un token fals, status code-ul asteptat fiind ‘401’ request 
invalid. Toate aceste teste au trecut cu success


Alte scenarii:

- test_scenario_1.py – testarea accesului clientilor la toate produsele fie accesand ‘all products’, fie ‘by 
category’(cazut – numarul produselor returnate ca lista complete de produse este diferit de suma 
numarului celor returnate pe categorie)

- test_scenario_2.py –testarea unicitatii id-ului produselor returnate (cazut – exista id folosit pentru 2 produse 
diferite)

- test_scenario_3.py – testarea adaugarii in cos a tuturor produselor cu id unic care sunt pe stoc, adaugarea de 
produse care nu sunt pe stoc , adaugarea tutror produselor din stoc indifferent de id(cade – exista 
id dublat, iar produsul cu id dublat nu mai poate fi adaugat in cos)

- test_scenario_4_e2e.py – este un test de tip ‘end to end’, se testeaza parcurgerea inlantuita a mai multor pasi: 
crearea uni cos, adaugarea de produse in cos, consultarea produselor aflate in cos, modificarea acestora, 
inlocuirea si stergerea de produse din cos, crearea unui cont, crearea unei comenzi, consultarea comenzilor, 
updatarea comenzii, stergerea comenzii
