## Example 2 - connecting Arduino to the ReFLeX.IoT without internet connect 

Neste exemplo, conectaremos o sensor de DHT ao ReFLeX.IoT usando Arduino através da Comunicação Serial.


**Passo a Passo para usar o Gateway**

1. Conecte seu arduino ao computador (desktop ou notebook)
 
2. Faça o Download do arquivo <a href="https://github.com/Rosiberto/Gateway-Serial-Port">ReFLeX.IoT-Gateway.exe</a> e execute-o 

3. Digite o número da Porta que o Arduino foi reconhecido e aperte ENTER

4. Informe:

	- URL Host , local onde está hospedado o ReFLeX.IoT;
	- Resource (Recurso);
	- API Key (Chave);
	- Device ID (ID do dispositivo).
	
	**Obs:** Resource, API Key e Device ID devem ser os mesmos cadastrados/gerados na UI do ReFLeX.IoT no menu ***Provisioning***.

5. Pronto!! Agora é só curtir!!!

6. Para finalizar o Gateway, basta pressionar a letra 'q'

7. No código do arduino, você deve informar TODOS os PARÂMETROS do AgentJSON a serem utilizados de acordo com o sensor, incluindo a eles, a leitura do sensor conforme exemplo abaixo:

<br>

**Exemplo - Sensor DHT**

```
void setup() {
  Serial.begin(9600);  
}

void loop() {

  // h = armazena a umidade   
  // t = armazena a temperatura 
  
  h = dht.readHumidity();
  t = dht.readTemperature();
  
  // "t:" e "h:" são os parâmetros que o agentJSON espera receber no ReFLeX.IoT
  Serial.println( String("t:")+t );
  
  // uma pausa entre os envios
  delay(5000); 
  
  Serial.println( String("h:")+h );
  delay(5000);  
```