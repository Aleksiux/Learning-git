# Studentų užduotis su lygmenimis

Sukurti Flask programą, kuri simuliuotų universiteto paskaitų registraciją tiek studentams, tiek dėstytojams. T.y., būtų galima prisiregistruoti prie esamų paskaitų studentams, ir nurodyti kurias paskaitas dėstytojai dėsto

## Level 1 (Pagrindai)
- Susikurti projekto struktūrą pagal atmintinę
- Susikonfiguruoti projektą `__init__.py` faile pagal atmintinę ir senus projektus
- Pasiimti `base.html` iš senų projektų, pakeisti atitinkamai užduočiai (sukurti studentų, dėstytojų, paskaitų įrašus navbare)
- Nenaudoti sqlalchemy duomenų bazių, vietoj to naudoti tik mock data dictionary, kuriuos nukopijuoti į `models.py` (vėliau į šį failą sudėsime duombazių modelius/lenteles)
```
students =[{
    'name': 'Jonas',
    'surname': 'Jonaitis'
},
{
    'name': 'Petras',
    'surname': 'Petraitis'
},
{
    'name': 'Auste',
    'surname': 'Austaityte'
},
{
    'name': 'Igne',
    'surname': 'Ignaityte'
}]

professors =[{
    'name': 'George',
    'surname': 'Washington',
    'experience': 12
},
{
    'name': 'Valdas',
    'surname': 'Adamkus',
    'experience': 25
},
{
    'name': 'Antanas',
    'surname': 'Smetona',
    'experience': 100
},
{
    'name': 'Jonas',
    'surname': 'Kubilius',
    'experience': 2
},
{
    'name': 'Algis',
    'surname': 'Algiauskas',
    'experience': 3
}]

lectures =[{
    'title': 'Introduction to Modal Logic'
},
{
    'title': 'Molecular Biology'
},
{
    'title': 'History of Lithuania'
},
{
    'title': 'Epidemiology'
}]
```
- Sukurti tris maršrutus kurie pasiimtų visus esančius duomenis iš paprasto atitinkamo dictionary (nurodyto žemiau) ir išrašytų kiekvieną įrašą atitinkamuose puslapiuose
- Sukurti tris atitinkamus templates, kurie gautų duomenis iš maršrutų funkcijų ir išrašytų visus įrašus kaip paragrafus ar sąrašus (`<ul>`)

## Level 2 (Duomenų saugojimas duombazėse)
- Sukurti DB modelius/lenteles studentams, dėstytojams, paskaitoms
- Ranka (per sqlalchemy ar per raw SQL) įrašyti tuos pačius duomenis į sukurtą DB failą 
- Išrašyti tuos duomenis atitinkamuose svetainės puslapiuose naudojant DB

## Level 3 (Duomenų įrašymas per formas)
- Pridėti Flask formas, per kurias būtų įmanoma išsaugoti studentus, dėstytojus ir paskaitas
- Atvaizduoti naujus, per formas įrašytus duomenis atitinkamuose puslapiuose

## Level 4 (Validatoriai formose, daugiaskaitiniai kintamieji duombazėse)
- Pridėti validatorius formose, jei dar to nepadarėte
- Kiekvienam dėstytojui leistų priskirti jo paskaitas (one2many ryšys)
- Kiekvienam studentui leistų priskirti daug paskaitų (many2many ryšys)

## Level 5 (Duomenų redagavimas) 
- Padaryti, kad būtų galima ištrinti dėstytojus, paskaitas, studentus
- Padaryti, kad būtų galima redaguoti dėstytojus, paskaitas, studentus

