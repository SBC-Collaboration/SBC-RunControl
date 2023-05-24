#include "MgsModbus.h"

// For Arduino 1.0
EthernetServer MbServer(MB_PORT);
// EthernetClient MbmClient;

// #define DEBUG2

MgsModbus::MgsModbus(word _MbDataLen, word *_MbData)
{
 
  MbDataLen = _MbDataLen;
  MbData = _MbData;
}


//****************** Recieve data for ModBusSlave ****************
void MgsModbus::MbsRun()
{  
  //****************** Read from socket ****************
  EthernetClient client = MbServer.available();
  if(client.available())
  {
    delay(10);
    int i = 0;
    while(client.available() && i<MBAS)
    {
      MbsByteArray[i] = client.read();
      i++;
    }
    if (i == MBAS) return; // data overrrun - ignore message

    MbsFC = SetFC(MbsByteArray[7]);  //Byte 7 of request is FC
  }


  
  int Start, WordDataLength, ByteDataLength, CoilDataLength, MessageLength;
  //****************** Read Coils (1 & 2) **********************
  if(MbsFC == MB_FC_READ_COILS || MbsFC == MB_FC_READ_DISCRETE_INPUT) {
    Start = word(MbsByteArray[8],MbsByteArray[9]);
    CoilDataLength = word(MbsByteArray[10],MbsByteArray[11]);
    ByteDataLength = CoilDataLength / 8;
    if(ByteDataLength * 8 < CoilDataLength) ByteDataLength++;      
    CoilDataLength = ByteDataLength * 8;
    MbsByteArray[5] = ByteDataLength + 3; //Number of bytes after this one.
    MbsByteArray[8] = ByteDataLength;     //Number of bytes after this one (or number of bytes of data).
    for(int i = 0; i < ByteDataLength ; i++)
    {
      MbsByteArray[9 + i] = 0; // To get all remaining not written bits zero
      for(int j = 0; j < 8; j++)
      {
        bitWrite(MbsByteArray[9 + i], j, GetBit(Start + i * 8 + j));
      }
    }
    MessageLength = ByteDataLength + 9;
    client.write(MbsByteArray, MessageLength);
    MbsFC = MB_FC_NONE;
  }
  //****************** Read Registers (3 & 4) ******************
  if(MbsFC == MB_FC_READ_REGISTERS || MbsFC == MB_FC_READ_INPUT_REGISTER) {
    Start = word(MbsByteArray[8],MbsByteArray[9]);
    #ifdef DEBUG2
    Serial.print("Read Start: "); Serial.println(Start);
    #endif
    WordDataLength = word(MbsByteArray[10],MbsByteArray[11]);
    #ifdef DEBUG2
    Serial.print("Read WordDataLength: "); Serial.println(WordDataLength);
    #endif
    ByteDataLength = WordDataLength * 2;
    MbsByteArray[5] = ByteDataLength + 3; //Number of bytes after this one.
    MbsByteArray[8] = ByteDataLength;     //Number of bytes after this one (or number of bytes of data).
    // check  and constrain boundary
    //  if (Start + WordDataLength > MbDataLen) WordDataLength = MbDataLen - Start;
          
    for(int i = 0; i < WordDataLength; i++)
    {
      MbsByteArray[ 9 + i * 2] = highByte(MbData[Start + i]);
      MbsByteArray[10 + i * 2] =  lowByte(MbData[Start + i]);
    }
    MessageLength = ByteDataLength + 9;
    client.write(MbsByteArray, MessageLength);
    MbsFC = MB_FC_NONE;
  }
  //****************** Write Coil (5) **********************
  if(MbsFC == MB_FC_WRITE_COIL) {
    Start = word(MbsByteArray[8],MbsByteArray[9]);
    if (word(MbsByteArray[10],MbsByteArray[11]) == 0xFF00){SetBit(Start,true);}
    if (word(MbsByteArray[10],MbsByteArray[11]) == 0x0000){SetBit(Start,false);}
    MbsByteArray[5] = 2; //Number of bytes after this one.
    MessageLength = 8;
    client.write(MbsByteArray, MessageLength);
    MbsFC = MB_FC_NONE;
  } 
  //****************** Write Register (6) ******************
  if(MbsFC == MB_FC_WRITE_REGISTER) {
    Start = word(MbsByteArray[8],MbsByteArray[9]);
    //if (Start < MbDataLen)  
    MbData[Start] = word(MbsByteArray[10],MbsByteArray[11]);
    MbsByteArray[5] = 6; //Number of bytes after this one.
    MessageLength = 12;
    client.write(MbsByteArray, MessageLength);
    MbsFC = MB_FC_NONE;
  }
  //****************** Write Multiple Coils (15) **********************
  if(MbsFC == MB_FC_WRITE_MULTIPLE_COILS) {
    Start = word(MbsByteArray[8],MbsByteArray[9]);
    CoilDataLength = word(MbsByteArray[10],MbsByteArray[11]);
    MbsByteArray[5] = 6;
    for(int i = 0; i < CoilDataLength; i++)
    {
      SetBit(Start + i,bitRead(MbsByteArray[13 + (i/8)],i-((i/8)*8)));
    }
    MessageLength = 12;
    client.write(MbsByteArray, MessageLength);
    MbsFC = MB_FC_NONE;
  }  
  //****************** Write Multiple Registers (16) ******************
  if(MbsFC == MB_FC_WRITE_MULTIPLE_REGISTERS) {
    Start = word(MbsByteArray[8],MbsByteArray[9]);
    #ifdef DEBUG2
    Serial.print("Write MRStart: "); Serial.println(Start);
    #endif
    WordDataLength = word(MbsByteArray[10],MbsByteArray[11]);
    ByteDataLength = WordDataLength * 2;
    MbsByteArray[5] = 6;
    // if (Start + WordDataLength > MbDataLen) WordDataLength = MbDataLen - Start;
    #ifdef DEBUG2
    Serial.print("Write MR WordDataLength: "); Serial.println(WordDataLength);
    #endif
    for(int i = 0; i < WordDataLength; i++)
    {
      MbData[Start + i] =  word(MbsByteArray[ 13 + i * 2],MbsByteArray[14 + i * 2]);
    }
    MessageLength = 12;
    client.write(MbsByteArray, MessageLength);
    MbsFC = MB_FC_NONE;
  }
}


//****************** ?? ******************
MB_FC MgsModbus::SetFC(int fc)
{
  MB_FC FC;
  FC = MB_FC_NONE;
   if(fc == 1) FC = MB_FC_READ_COILS;
   if(fc == 2) FC = MB_FC_READ_DISCRETE_INPUT;
  if(fc == 3) FC = MB_FC_READ_REGISTERS;
  if(fc == 4) FC = MB_FC_READ_INPUT_REGISTER;
   if(fc == 5) FC = MB_FC_WRITE_COIL;
  if(fc == 6) FC = MB_FC_WRITE_REGISTER;
   if(fc == 15) FC = MB_FC_WRITE_MULTIPLE_COILS;
  if(fc == 16) FC = MB_FC_WRITE_MULTIPLE_REGISTERS;
  return FC;
}

 
word MgsModbus::GetDataLen()
{
  return MbDataLen;
}

 
boolean MgsModbus::GetBit(word Number)
{
  int ArrayPos = Number / 16;
  int BitPos = Number - ArrayPos * 16;
  boolean Tmp = bitRead(MbData[ArrayPos],BitPos);
  return Tmp;
}


boolean MgsModbus::SetBit(word Number,boolean Data)
{
  int ArrayPos = Number / 16;
  int BitPos = Number - ArrayPos * 16;
  boolean Overrun = ArrayPos > MbDataLen * 16; // check for data overrun
  if (!Overrun){                 
    bitWrite(MbData[ArrayPos],BitPos,Data);
  } 
  return Overrun;
}
