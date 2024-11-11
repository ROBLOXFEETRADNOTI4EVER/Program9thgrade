const int trigPin = 9;
const int echoPin = 10;
const int niggerPin = 11;
const int Patrik = 13;
// declaring the colors 
const int blue = 2;
const int green = 3;
const int red = 4;

int rd = 0;
int gr = 255;
int bl = 0;

void setup(){
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(niggerPin, OUTPUT);
  pinMode(Patrik, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(red, OUTPUT);

}

void setRGB(int rd, int gr, int bl)
 {
    analogWrite(red, rd);
      analogWrite(green, gr);
      analogWrite(blue, bl);
}

void loop(){


  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(trigPin, LOW);

  

  float t = pulseIn(echoPin, HIGH);
  float distance = t*0.017015;
  Serial.print("Distance: ");
  Serial.println(distance);

  if(distance < 23 && distance > 16){
      digitalWrite(niggerPin, HIGH);
      tone(5, 700, 250);
          tone(5, 500, 400);
      tone(5, 600, 500);
      rd = 0;
      gr = 255;
      bl = 150;
  }
  else if (distance < 16 && distance > 10){
          digitalWrite(niggerPin, HIGH);
      tone(5, 1252, 250);
      tone(5, 1352, 280);
      tone(5, 1252, 300);
      tone(5, 1352, 320);
      delay(100);
      rd = 255,5;
      gr = 100,5;
      bl = 150;

      setRGB(rd,gr,bl);
      


  }
  else if (distance < 9 && distance > 0){
          digitalWrite(niggerPin, HIGH);
      tone(5, 1252, 250);
      tone(5, 1352, 280);
      tone(5, 1252, 300);
      tone(5, 1352, 320);
      delay(100);
      rd = 255;
      gr = 0;
      bl = 0;

      setRGB(rd,gr,bl);
  


  }




    else{
      setRGB(rd,gr,bl);
      rd = 0;
      gr = 255;
      bl = 100;

    
    }

   
  
}
