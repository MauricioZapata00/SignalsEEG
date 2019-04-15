# -*- coding: utf-8 -*-
"""
@authors: Johana Córdoba Lemus
          Mauricio Zapata Contreras
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import scipy.stats
import LinearFIR
class Global(object):
    def __init__(self,Txt,String,Lista,Vector,Tiempo,Pos,Dict,Frec,TGra,Dict_2,Lista_2):
        super(Global,self).__init__();
        self.__El_Text=Txt;
        self.__El_String=String;
        self.__La_Lista=Lista;
        self.__El_Vector=Vector;
        self.__El_Tiempo=Tiempo;
        self.__La_Pos=Pos;
        self.__El_Dict=Dict;
        self.__La_Frec=Frec;
        self.__El_TGra=TGra;
        self.__El_Dict_2=Dict_2;
        self.__La_Lista_2=Lista_2;
    def Cargar_Datos(self,Archivo):
        self.__El_Text=open(Archivo);
        self.__El_String=self.__El_Text.readlines();
        self.__El_Text.close();
        self.__El_String=str(self.__El_String).split(',');
        self.__La_Lista=list(self.__El_String);
        self.__La_Lista=list(self.__La_Lista[6:]);
        return(self.__La_Lista);
        self.__El_Text=0;
        self.__El_String=0;
        self.__El_String=0;
        self.__La_Lista=0;
    def Convertir_Datos(self,Datos):
        self.__El_Vector=np.zeros([len(Datos),8]);
        self.__La_Pos=1;
        for i in np.arange(0,len(Datos)-1,1):
            self.__El_Vector[i]=Datos[self.__La_Pos:self.__La_Pos+8];
            self.__La_Pos=self.__La_Pos+13;
            if(self.__La_Pos>len(Datos)):
                self.__El_Vector=self.__El_Vector[0:i+1];
                break;
        for i in np.arange(0,8,1):
            self.__El_Dict.setdefault('Canal'+str(i+1),self.__El_Vector[0:,i]);
        return(self.__El_Dict);
        self.__El_Vector=0;
        self.__La_Pos=0;
        self.__El_Dict.clear();
    
    def Graficar_Datos(self,t,d):
        self.__El_Tiempo=t;
        self.__El_Dict=d.copy();
        self.__La_Frec=(len(self.__El_Dict['Canal1']))/self.__El_Tiempo;
        self.__El_TGra=np.arange(0,self.__El_Tiempo,1/self.__La_Frec);
        #self.__El_Vector=self.Get_Keys(self.__El_Dict);
        for i in np.arange(0,len(self.__El_Dict),1):
            plt.plot(self.__El_TGra,self.__El_Dict['Canal'+str(i+1)]);
            plt.hold(True);
        plt.hold(False);
        plt.title('Señal con Todos los canales');
        plt.xlabel("Tiempo [s]");
        plt.ylabel("Voltios [uV]");
        plt.legend(['Canal1','Canal2','Canal3','Canal4','Canal5','Canal6','Canal7','Canal8'],loc='best');
        plt.show();
        self.__El_Tiempo=0;
        self.__El_Dict.clear();
        self.__La_Frec=0;
        self.__El_TGra=0;
    def Segmentar_Canal(self,Dic,Seg):
        self.__El_Dict=Dic.copy();
        self.__La_Lista=self.__El_Dict.get('Canal1');
        if(len(self.__La_Lista)==51424):
            __T_Seg=5.625;
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict.get('Canal'+str(i+1));
                self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                self.__El_Dict['Canal'+str(i+1)]=self.__La_Lista_2[Seg-1];
                self.__El_TGra=np.linspace(__T_Seg*(Seg-1),__T_Seg*(Seg),1607);
                plt.plot(self.__El_TGra,(100*i)+self.__La_Lista_2[Seg-1]);
                plt.hold(True);
            plt.hold(False);
            plt.title('Señal de Segmento '+str(Seg));
            plt.xlabel("Tiempo [s]");
            plt.ylabel("Voltios [uV]");
            plt.legend(['Canal1','Canal2','Canal3','Canal4','Canal5','Canal6','Canal7','Canal8'],loc='best');
            plt.show();
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__El_Dict_2.clear();
            self.__La_Lista=0;
            self.__El_TGra=0;
            self.__La_Lista_2=0;
        
        if(len(self.__La_Lista)==31012):
            __T_Seg=4.8;
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict.get('Canal'+str(i+1));
                self.__La_Lista=self.__La_Lista[0:31000];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                self.__El_Dict['Canal'+str(i+1)]=self.__La_Lista_2[Seg-1];
                self.__El_TGra=np.linspace(__T_Seg*(Seg-1),__T_Seg*(Seg),1240);
                plt.plot(self.__El_TGra,(100*i)+self.__La_Lista_2[Seg-1]);
                plt.hold(True);
            plt.hold(False);
            plt.title('Señal de Segmento '+str(Seg));
            plt.xlabel("Tiempo [s]");
            plt.ylabel("Voltios [uV]");
            plt.legend(['Canal1','Canal2','Canal3','Canal4','Canal5','Canal6','Canal7','Canal8'],loc='best');
            plt.show();
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__El_Dict_2.clear();
            self.__La_Lista=0;
            self.__El_TGra=0;
            self.__La_Lista_2=0;
        
        if(len(self.__La_Lista)==794648):
            __T_Seg=1590/361;
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict.get('Canal'+str(i+1));
                self.__La_Lista=self.__La_Lista[0:794200];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                self.__El_Dict['Canal'+str(i+1)]=self.__La_Lista_2[Seg-1];
                self.__El_TGra=np.linspace(__T_Seg*(Seg-1),__T_Seg*(Seg),1100);
                plt.plot(self.__El_TGra,(100*i)+self.__La_Lista_2[Seg-1]);
                plt.hold(True);
            plt.hold(False);
            plt.title('Señal de Segmento '+str(Seg));
            plt.xlabel("Tiempo [s]");
            plt.ylabel("Voltios [uV]");
            plt.legend(['Canal1','Canal2','Canal3','Canal4','Canal5','Canal6','Canal7','Canal8'],loc='best');
            plt.show();
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__El_Dict_2.clear();
            self.__La_Lista=0;
            self.__El_TGra=0;
            self.__La_Lista_2=0;
        
        if(len(self.__La_Lista)==31113):
            __T_Seg=4.8;
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict.get('Canal'+str(i+1));
                self.__La_Lista=self.__La_Lista[0:31100];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                self.__El_Dict['Canal'+str(i+1)]=self.__La_Lista_2[Seg-1];
                self.__El_TGra=np.linspace(__T_Seg*(Seg-1),__T_Seg*(Seg),1244);
                plt.plot(self.__El_TGra,(100*i)+self.__La_Lista_2[Seg-1]);
                plt.hold(True);
            plt.hold(False);
            plt.title('Señal de Segmento '+str(Seg));
            plt.xlabel("Tiempo [s]");
            plt.ylabel("Voltios [uV]");
            plt.legend(['Canal1','Canal2','Canal3','Canal4','Canal5','Canal6','Canal7','Canal8'],loc='best');
            plt.show();
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__El_Dict_2.clear();
            self.__La_Lista=0;
            self.__El_TGra=0;
            self.__La_Lista_2=0;
    
    def Filtrar(self,Dic):
        self.__El_Dict=Dic.copy();
        #self.__El_Dict_2.clear();
        #self.__El_Vector=self.Get_Keys(self.__El_Dict);
        for i in np.arange(0,len(self.__El_Dict),1):
            self.__La_Lista=self.__El_Dict.get('Canal'+str(i+1));
            self.__La_Lista_2=LinearFIR.eegfiltnew(self.__La_Lista,250,50,0.5);
            self.__El_Dict_2.setdefault('Canal'+str(i+1),self.__La_Lista_2);
        return(self.__El_Dict_2);
        self.__El_Dict.clear();
        self.__El_Dict_2.clear();
        self.__La_Lista=0;
        self.__La_Lista_2=0;
    def Potencia(self,Dic):
        self.__El_Dict=Dic.copy();
        #self.__El_Vector=self.Get_Keys(self.__El_Dict);
        for i in np.arange(0,len(self.__El_Dict),1):
            self.__La_Frec,self.__La_Pos=signal.welch(self.__El_Dict['Canal'+str(i+1)],250,'hanning');
            self.__El_Dict_2.setdefault('Canal'+str(i+1),self.__La_Pos);
            plt.plot(self.__La_Frec,self.__La_Pos+(10*i));
            plt.hold(True);
        plt.legend(['Canal1','Canal2','Canal3','Canal4','Canal5','Canal6','Canal7','Canal8'],loc='best');
        plt.title('Periodograma');
        plt.xlabel("Frecuencia [Hz]");
        plt.ylabel("Potencia [W]");
        plt.show();
        return(self.__El_Dict_2);
        self.__El_Dict.clear();
        self.__El_Dict_2.clear();
        self.__La_Frec=0;
        self.__La_Pos=0;
        
    def Delete_Umbral(self,Dic,Umb):
        self.__El_Dict=Dic.copy();
        self.__La_Lista=self.__El_Dict['Canal1'];
        __Array=[[],[],[],[],[],[],[],[]];
        __Cont=0;
        print(len(self.__La_Lista));
        
        if(len(self.__La_Lista==51424)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=np.max(self.__El_Vector);
                    self.__La_Frec=np.min(self.__El_Vector);
                    if((self.__La_Pos>Umb) or (self.__La_Frec<-Umb)):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==31012)):
            __Cont=0;
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:31000];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=np.max(self.__El_Vector);
                    self.__La_Frec=np.min(self.__El_Vector);
                    if((self.__La_Pos>Umb) or (self.__La_Frec<-Umb)):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==794648)):
            __Cont=0;
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:794200];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                #print(len(self.__La_Lista_2));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=np.max(self.__El_Vector);
                    self.__La_Frec=np.min(self.__El_Vector);
                    if((self.__La_Pos>Umb) or (self.__La_Frec<-Umb)):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==31113)):
            __Cont=0;
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:31100];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                #print(len(self.__La_Lista_2));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=np.max(self.__El_Vector);
                    self.__La_Frec=np.min(self.__El_Vector);
                    if((self.__La_Pos>Umb) or (self.__La_Frec<-Umb)):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
    
    def Delete_Pen(self,Dic,Pen):
        self.__El_Dict=Dic.copy();
        self.__La_Lista=self.__El_Dict['Canal1'];
        __Array=[[],[],[],[],[],[],[],[]];
        __Cont=0;
        print(len(self.__La_Lista));
        
        if(len(self.__La_Lista==51424)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=signal.detrend(self.__El_Vector);
                    self.__La_Frec=(self.__La_Pos[len(self.__La_Pos)-1]-self.__La_Pos[0])/5.625;
                    if(self.__La_Frec>Pen):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==31012)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:31000];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=signal.detrend(self.__El_Vector);
                    self.__La_Frec=(self.__La_Pos[len(self.__La_Pos)-1]-self.__La_Pos[0])/4.8;
                    if(self.__La_Frec>Pen):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==794648)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:794200];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=signal.detrend(self.__El_Vector);
                    self.__La_Frec=(self.__La_Pos[len(self.__La_Pos)-1]-self.__La_Pos[0])/(1590/361);
                    if(self.__La_Frec>Pen):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==31113)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:31100];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=signal.detrend(self.__El_Vector);
                    self.__La_Frec=(self.__La_Pos[len(self.__La_Pos)-1]-self.__La_Pos[0])/4.8;
                    if(self.__La_Frec>Pen):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
    def Delete_Kurt(self,Dic,Kur):
        self.__El_Dict=Dic.copy();
        self.__La_Lista=self.__El_Dict['Canal1'];
        __Array=[[],[],[],[],[],[],[],[]];
        __Cont=0;
        print(len(self.__La_Lista));
        
        if(len(self.__La_Lista==51424)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=scipy.stats.kurtosis(self.__El_Vector);
                    self.__La_Frec=np.mean(self.__La_Pos);
                    if(abs(self.__La_Frec)<Kur):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==31012)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:31000];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=scipy.stats.kurtosis(self.__El_Vector);
                    self.__La_Frec=np.mean(self.__La_Pos);
                    if(abs(self.__La_Frec)<Kur):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==794648)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:794200];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=scipy.stats.kurtosis(self.__El_Vector);
                    self.__La_Frec=np.mean(self.__La_Pos);
                    if(abs(self.__La_Frec)<Kur):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==31113)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:31100];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Pos=scipy.stats.kurtosis(self.__El_Vector);
                    self.__La_Frec=np.mean(self.__La_Pos);
                    if(abs(self.__La_Frec)<Kur):
                        print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                        for k in np.arange(0,len(self.__El_Dict),1):
                            if(__Cont==0):
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                            else:
                                self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                                self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                __Array[k]=np.ravel(self.__La_Lista_2);
                        __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
    
    def Delete_Pot(self,Dic,Pot):
        self.__El_Dict=Dic.copy();
        self.__La_Lista=self.__El_Dict['Canal1'];
        __Array=[[],[],[],[],[],[],[],[]];
        __Cont=0;
        print(len(self.__La_Lista));
        
        if(len(self.__La_Lista==51424)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Frec,self.__La_Pos=signal.welch(self.__El_Vector,250,'hanning');
                    self.__El_Tiempo=np.mean(self.__La_Pos);
                    for l in np.arange(0,len(self.__La_Pos),1):
                        if(self.__La_Pos[l]>Pot):
                            print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                            for k in np.arange(0,len(self.__El_Dict),1):
                                if(__Cont==0):
                                    self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                    self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                                    self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                    __Array[k]=np.ravel(self.__La_Lista_2);
                                else:
                                    self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                    self.__La_Lista_2=np.reshape(self.__La_Lista,(32,1607));
                                    self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                    __Array[k]=np.ravel(self.__La_Lista_2);
                            __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==31012)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:31000];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Frec,self.__La_Pos=signal.welch(self.__El_Vector,250,'hanning');
                    self.__El_Tiempo=np.mean(self.__La_Pos);
                    for l in np.arange(0,len(self.__La_Pos),1):
                        if(self.__La_Pos[l]>Pot):
                            print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                            for k in np.arange(0,len(self.__El_Dict),1):
                                if(__Cont==0):
                                    self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                    self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                                    self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                    __Array[k]=np.ravel(self.__La_Lista_2);
                                else:
                                    self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                    self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1240));
                                    self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                    __Array[k]=np.ravel(self.__La_Lista_2);
                            __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==794648)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:794200];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Frec,self.__La_Pos=signal.welch(self.__El_Vector,250,'hanning');
                    self.__El_Tiempo=np.mean(self.__La_Pos);
                    for l in np.arange(0,len(self.__La_Pos),1):
                        if(self.__La_Pos[l]>Pot):
                            print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                            for k in np.arange(0,len(self.__El_Dict),1):
                                if(__Cont==0):
                                    self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                    self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                                    self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                    __Array[k]=np.ravel(self.__La_Lista_2);
                                else:
                                    self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                    self.__La_Lista_2=np.reshape(self.__La_Lista,(722,1100));
                                    self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                    __Array[k]=np.ravel(self.__La_Lista_2);
                            __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
        
        if(len(self.__La_Lista==31113)):
            for i in np.arange(0,len(self.__El_Dict),1):
                self.__La_Lista=self.__El_Dict['Canal'+str(i+1)];
                self.__La_Lista=self.__La_Lista[0:31100];
                self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                for j in np.arange(0,len(self.__La_Lista_2),1):
                    self.__El_Vector=self.__La_Lista_2[j-1];
                    self.__La_Frec,self.__La_Pos=signal.welch(self.__El_Vector,250,'hanning');
                    self.__El_Tiempo=np.mean(self.__La_Pos);
                    for l in np.arange(0,len(self.__La_Pos),1):
                        if(self.__La_Pos[l]>Pot):
                            print('Época Eliminada: '+str(j+1)+' del Canal'+str(i+1));
                            for k in np.arange(0,len(self.__El_Dict),1):
                                if(__Cont==0):
                                    self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                    self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                                    self.__La_Lista_2=np.delete(self.__La_Lista_2,j,0);
                                    __Array[k]=np.ravel(self.__La_Lista_2);
                                else:
                                    self.__La_Lista=self.__El_Dict['Canal'+str(k+1)];
                                    self.__La_Lista_2=np.reshape(self.__La_Lista,(25,1244));
                                    self.__La_Lista_2=np.delete(self.__La_Lista_2,j-__Cont,0);
                                    __Array[k]=np.ravel(self.__La_Lista_2);
                            __Cont=__Cont+1;
            for i in np.arange(0,len(__Array),1):
                self.__El_Dict['Canal'+str(i+1)]=__Array[i];
            return(self.__El_Dict);
            self.__El_Dict.clear();
            self.__La_Lista=0;
            self.__La_Lista_2=0;
            self.__El_Vector=0;
            self.__La_Frec=0;
            self.__La_Pos=0;
            
Data_1="P1_RAWEEG_2018-11-15_Electrobisturí1_3min.txt";###180s=3min
Data_2="P1_RAWEEG_2018-11-15_Electrobisturí2_2min.txt";###120s=2min
Data_Fin="P1_RAWEEG_2018-11-15_FinProcedimiento_53min.txt";###3180s=53min
Data_Ojos="P1_RAWEEG_2018-11-15_OjosCerrados_2min.txt";###120s=2min
Var_1=Global(0,0,0,0,0,0,{},0,0,{},0);
S=Var_1.Cargar_Datos(Data_1);
D=Var_1.Convertir_Datos(S);
Var_1.Graficar_Datos(180,D);
D_F=Var_1.Filtrar(D);
D_S=Var_1.Segmentar_Canal(D_F,4);
D_Pot=Var_1.Potencia(D_S);
D_U=Var_1.Delete_Umbral(D_F,100);
D_P=Var_1.Delete_Pen(D_F,4);
D_K=Var_1.Delete_Kurt(D_F,0.1);
D_W=Var_1.Delete_Pot(D_F,30);
D_Pot=Var_1.Potencia(D_W);







  
    
    

