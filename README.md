# Wørdle på dansk

En undersøgelse af hvilke to ord der mest optimalt skal testes som de første i Wørdle på dansk. Analysen er baseret på en frekvens optælling af bogstaver i de danske ord.

De danske ord er taget fra retskrivningsordbogens online version på https://roplus.dk/#ordbog/ 


## Prepare for Digital Ocean

docker tag wordledk registry.digitalocean.com/uggiuggi/wordledk ; docker push registry.digitalocean.com/uggiuggi/wordledk

## Run command
uvicorn app:app --host 0.0.0.0 --port 8080