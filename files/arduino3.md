## Example 3 - connecting Arduino to the ThingSpeak without internet connect 

# ThingSpeak Gateway Serial Port
(by Rosiberto Santos)


**Passo a Passo para usar o Gateway**

1. Conecte seu arduino ao computador (desktop ou notebook)
 
2. Faça o Download do arquivo <a href="https://github.com/Rosiberto/Gateway-Serial-Port"> ThingSpeak-Gateway.exe</a> e execute-o 

3. Digite o número da Porta que o Arduino foi reconhecido e aperte ENTER

4. Informe o Canal do ThingSpeak para qual deseja enviar os dados e aperte ENTER

5. Informe a sua Write Api Key para conseguir salvar os dados no canal e pressione ENTER

6. Pronto!! Agora é só curtir!!!

7. Para finalizar o Gateway, basta pressionar a letra 'q'

8. No código do arduino, você deve informar TODOS os FIELDS do ThingSpeak que serão utilizados, incluindo a eles, a leitura do sensor conforme exemplo abaixo:



**Para um sensor**

```
void setup() {
  Serial.begin(9600);  
}

  void loop() {
  
  //faz a leitura de um sensor analógico qualquer 
  leituraSensor = analogRead(porta_sensor);
  
  // escreve o valor lido pelo sensor na serial concatenado ao field1
  // este field1 refere-se ao field1 do ThingSpeak que armazenará o resultado na nuvem
  Serial.println( String("field1:")+leituraSensor );

  // aguarda 15seg para enviar a próxima leitura
  delay(15000);
}
```

<br>

**Para vários sensores**
```
void setup() {
  Serial.begin(9600);  
}

  void loop() {
  
  leituraSensor1 = analogRead(porta_sensor1);
  leituraSensor2 = digitalRead(porta_sensor2);
  leituraSensor3 = analogRead(porta_sensor3);
  
  // escreve o valor lido pelo sensor na serial  
  Serial.println( String("field1:")+leituraSensor1 );  
  
  // aguarda 15seg para enviar a leitura do próximo sensor
  delay(15000);
  
  // os passos se repetem
  Serial.println( String("field2:")+leituraSensor2 );  
  delay(15000);
  
  Serial.println( String("field3:")+leituraSensor3 );  
  delay(15000);
  
  
}
```


