## Example 1 - connecting Arduino to the ReFLeX.IoT with internet connect 

Neste exemplo, conectaremos o sensor de nível ao ReFLeX.IoT usando Arduino.


*1 - Inclusão das Bibliotecas*
```
#include <WiFi.h> 
#include <HTTPClient.h> 
#include <ArduinoJson.h> 
#include <ArduinoJson.hpp> 
``` 

*2 - Definição das variáveis, constantes, credenciais de rede e url*

``` 
const char* ssid     = "XXXX"; 
const char* password = "XXXX"; 
 
//IP_ReFLeX.IoT - host onde o ReFLeX.IoT está instalado (e.g. localhost)
//PORTA         - onde o AgentJson espera receber os dados do sensor
//RESOURCE      - (e.g. /iot/json) recurso cadastrado no Service Group 
//DEVICE_ID     - device cadastrado no Device
//APIKEY        - chave gerada pelo ReFLeX.IoT

String IP_ReFLeX.IoT = "yyyyyyy"
String PORTA         = "7896"
String RESOURCE      = "zzzzzzz"
String DEVICE_ID     = "wwwwwww"
String APIKEY        = "kkkkkkk"


//definição da URL completa. Não alterar
String url = "http://"+IP_ReFLeX.IoT+":"+PORTA+RESOURCE+"?i="+DEVICE_ID+"&k="+APIKEY; 
 

//Variáveis de tempo 
unsigned long lastTime = 0; 
unsigned long timerDelay = 30000;

/* Pinos correspondentes ao sensor */
#define sensorVCC 2     /*Define vcc como pino 2 */ 
#define sensorSinal A1  /*Define sinal como pino A1 */ 

```

*3 - Configurações*
```
void setup() { 

  Serial.begin(9600);

  /* define 2 como pino de saída do Arduino */
  pinMode(sensorvcc, OUTPUT);

  /* vcc tem nível lógico baixo até que haja alguma variação na leitura */
  digitalWrite(sensorvcc, LOW);   
    
 
  WiFi.begin(ssid, password); 
  Serial.println("Conectando..."); 
  
  while(WiFi.status() != WL_CONNECTED) { 
    delay(500); 
    Serial.print("."); 
  } 
  
  Serial.println(""); 
  Serial.print("Conectado a WiFi com IP: "); 
  Serial.println(WiFi.localIP()); 
   
} 
```
 
 
*4 - Medições e Envio*
```
void loop() { 

  if ((millis() - lastTime) > timerDelay) { 
  
    //Verifica o estado da conexão WiFi 
    if(WiFi.status()== WL_CONNECTED){
		
      HTTPClient http; 
      String urlPath = url; 
	  
      delay(5000); 
      
	  //captura a leitura do sensor
	  int l = leituraSensorNivel() ;  
              
	  if ( isnan(l) ) {

		  Serial.println("Erro ao obter dados do sensor de nível");       
		  return; 

    } 	  
	  
    http.begin( urlPath.c_str() ); 	  
	  http.addHeader("Content-Type", "application/json"); 
	  http.addHeader("fiware-service", "reflexiot");
	  http.addHeader("fiware-servicepath", "/");
 
    // Coloca a leitura do sensor no formato JSON 
    String json; 
    DynamicJsonDocument doc(1024); 
	  
    doc["l"]= l; 
      
    serializeJson(doc, json); 
	  
	  //mostra no serial monitor o valor lido no formato json
    Serial.println(json); 
 
	  //envia para o ReFLeX.IoT
    int httpResponseCode = http.POST(json);  

	  //retorno da solicitação
    if (httpResponseCode > 0) { 
	  
      Serial.print("HTTP Response code: "); 
      Serial.println(httpResponseCode); 
      String payload = http.getString(); 
      Serial.println(payload); 
     
	  }else{ 
      Serial.print("Error code: "); 
      Serial.println(httpResponseCode); 
    } 
      
	    http.end();
    } 
    else { 
      Serial.println("WiFi Desconectado"); 
    } 
	
    lastTime = millis(); 
	
  } 
} 
```


*5 - Coleta das leituras*
```
int leituraSensorNivel() {  
 digitalWrite(sensorVCC, HIGH); /* alimenta o sensor */
 delay(10);              		    /* espera 10ms */
 val = analogRead(sensorSinal); /* Faz a leitura analógica do sensor */
 digitalWrite(sensorVCC, LOW);  /* Desliga o sensor */
 
 return val;             		    /* envia leitura */
}
```