# PDF Cleaner

PDF Cleaner je jednoduchá webová aplikace napsaná v Pythonu s využitím frameworku Flask. Umožňuje uživatelům nahrávat PDF soubory, které jsou poté "očištěny" - převedeny na obrázky a zpět do formátu PDF. Tento proces odstraňuje veškerý text a ponechává pouze vizuální obsah.

## Funkce

- Nahrávání PDF souborů.
- Automatické "očištění" PDF od textu, ponechání pouze obrázkového obsahu.
- Možnost stáhnout očištěné PDF.

## Jak začít

### Požadavky

- Docker
- Git (volitelně, pro klonování repozitáře)

### Sestavení a spuštění s Dockerem

```bash
docker run -d -p 5000:5000 --name pdf_cleaner newpaw/pdf_cleaner_app:latest
```
Tento příkaz stáhne Docker image newpaw/pdf_cleaner_app:latest z Docker Hubu (pokud ještě není lokálně dostupný) a spustí kontejner s názvem pdf_cleaner. Aplikace bude dostupná na http://localhost:5000.

## Licence
Tento projekt je volně dostupný a může být použit kýmkoliv dalším. Užijte si svobodu s PDF Cleaner!