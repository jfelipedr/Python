#######################################################
# Airplane performance calculator code                #
# Author: Jaime Alberto Escobar G.                    #
# Date: April, 2018                                   #
#######################################################

# Atmosphere function definition

T0 = 288.15
P0 = 101325
rho0 = 1.225
R = 287.058
l = 0.0065
g = 9.807
gama = 1.4
a0 = ( gama * R * T0 )**0.5
import math
from math import log, atan, sin, cos, asin, acos, pi, tan

def atmosphere ( hp, deltaT, RH ):
        if hp < 11000:
                Tsta = T0 - l * hp
                T = Tsta + deltaT
                P = P0 * ( 1 - ( l * hp ) / T0 ) ** ( g / ( l * R ) )
        else:
                Tsta = T0 - l * 11000
                T = Tsta + deltaT
                Ptr = P0 * ( 1 - ( l * 11000 ) / T0 ) ** ( g / ( l * R ) )
                P = Ptr * math.exp ( - g / ( R * T ) * ( hp - 11000 ))
        ES = 6.1078 * 10 ** (7.5 * (T - 273.15)/(237.3 + (T - 273.15)))
        Pv = ES * RH * 100
        rho = ( P / ( R * T ) ) * (1 - ( 0.378 * Pv ) / P )
        a = ( gama * R * T )**0.5
        print ("T = %7.2f" % T, "P = %10.2f" % P, "rho = %6.3f" % rho, "a = %7.2f" % a)
        return T,P,rho,a

# atmospheric properties based on geometric altitude
        
def atmospherehg ( hg, deltaT, RH, PSL ):
        if hg < 11000:
                Tsta = T0 - l * hg
                T = Tsta + deltaT
                TSL = 288.15 + deltaT
                P = PSL * ( 1 - ( l * hg ) / TSL ) ** ( g / ( l * R ) )
        else:
                Tsta = T0 - l * 11000
                T = Tsta + deltaT
                Ptr = P0 * ( 1 - ( l * 11000 ) / T0 ) ** ( g / ( l * R ) )
                P = Ptr * math.exp ( - g / ( R * T ) * ( hp - 11000 ))
        ES = 6.1078 * 10 ** (7.5 * (T - 273.15)/(237.3 + (T - 273.15)))
        Pv = ES * RH * 100
        rho = ( P / ( R * T ) ) * (1 - ( 0.378 * Pv ) / P )
        a = ( gama * R * T )**0.5
        hp = ( 1 - (P / P0)**( l * R / g) ) * (T0 / l)
        print ("T = %7.2f" % T, "P = %10.2f" % P, "rho = %6.3f" % rho, "a = %7.2f" % a, "hp = %6.1f" % hp)
        return T,P,rho,a,hp

# IAS to TAS function definition

def IAStoTAS (hp, deltaT, RH, IAS, deltaVi, deltaVp):
#        T0 = 288.15
#        P0 = 101325
#        rho0 = 1.225
#        R = 287.058
#        gama = 1.4
#        a0 = ( gama * R * T0 )**0.5
        T,P,rho,a = atmosphere (hp, deltaT, RH)
        CAS = IAS + deltaVi + deltaVp
        qc = P0 * ((1 + ((gama - 1) / 2) * (CAS / a0)**2 )**(gama / (gama - 1)) - 1)
        EAS = ( (2 * gama / (gama - 1)) * (P / rho0) * ((qc / P + 1)**( (gama - 1) / gama) - 1) )**0.5
        TAS = EAS / (rho / rho0)**0.5
        print ("CAS = %3.2f" % CAS, "qc = %8.2f" % qc, "EAS = %3.2f" % EAS, "TAS = %3.2f" % TAS)
        return CAS,qc,EAS,TAS

# TAS to IAS function definition

def TAStoIAS (hp, deltaT, RH, TAS, deltaVi, deltaVp):
#        T0 = 288.15
#        P0 = 101325
#        rho0 = 1.225
#        R = 287.058
#        gama = 1.4
#        a0 = ( gama * R * T0 )**0.5
        T,P,rho,a = atmosphere (hp, deltaT, RH)
        EAS = TAS * (rho / rho0)**0.5
        qc = (( EAS**2 * ((gama - 1) / (2 * gama)) * (rho0 / P) + 1)**(gama / (gama - 1)) - 1 ) * P
        CAS = ((( (qc / P0) + 1)**((gama - 1) / gama) - 1) * 2 / (gama - 1))**0.5 * a0
        IAS = CAS - deltaVi - deltaVp
        print ("EAS = %3.2f" % EAS, "qc = %8.2f" % qc, "CAS = %3.2f" % CAS, "IAS = %3.2f" % IAS)
        return EAS,qc,CAS,IAS

# Stall speed
        
def Vstall (hp, deltaT, RH, W, S, CLmax):
        T,P,rho,a = atmosphere (hp, deltaT, RH)
        Vs = ( (2/rho) * (W/S) * (1/CLmax) )**0.5
        print ("Vstall = %3.2f" % Vs)
        return Vs

# Minimum required thrust
        
def MinThrust (hp, deltaT, RH, CDo, K, W, S):
#        T0 = 288.15
#        P0 = 101325
#        rho0 = 1.225
#        R = 287.058
#        gama = 1.4
#        a0 = ( gama * R * T0 )**0.5
        T,P,rho,a = atmosphere (hp, deltaT, RH)
        LDmax = 1 / ( 4 * K * CDo )**0.5
        THmin = W / LDmax
        VLDmax = (( 2/rho) * (K / CDo)**0.5 * (W / S) )**0.5
        CLLDmax = ( CDo / K)**0.5
        print ("L/Dmax = %3.2f" % LDmax, "THmin = %7.2f" % THmin, "VL/Dmax = %4.2f" % VLDmax, "CL L/Dmax = %2.4f" % CLLDmax)
        return LDmax,THmin,VLDmax, CLLDmax

# Minimum required power
        
def Pmin (hp, deltaT, RH, CDo, K, W, S):
        T,P,rho,a = atmosphere (hp, deltaT, RH)
        CL32CDmax = ( 1/4 ) * (3 / ( K * CDo**(1/3) ) )**(3/4)
        Potmin = (1 / CL32CDmax) * ( 2 * W**3 / (rho * S ) )**0.5
        VCLCD32max = ( (2/rho) * (K / (3 * CDo) )**0.5 * (W/S) )**0.5
        CLPmin = (3 * CDo / K)**0.5
        print ("CL^3/2/CD = %3.2f" % CL32CDmax, "PRmin = %7.2f" % Potmin, "V CL^3/2/CDmax %4.2f" % VCLCD32max, "CLPmin = %2.4f" % CLPmin)
        return CL32CDmax,Potmin,VCLCD32max,CLPmin

# Available thrust turbojet
        
def ThrustTJ (hp, deltaT, RH, V, Thstat, TR):
        T,P,rho,a = atmosphere (hp, deltaT, RH)
        M = V / a
        theta0 = (T / 288.15) * (1 + ((1.4 - 1) / 2) * M**2)
        delta0 = (P / 101325) * (1 + ((1.4 - 1) / 2) * M**2) ** (1.4 / 0.4)
        if theta0 <= TR:
                TA = 0.8 * Thstat * delta0 * (1 - 0.16 * M**0.5)
        else:
                TA = 0.8 * Thstat * delta0 * (1 - 0.16 * M**0.5 - 24 * (theta0 - TR) / ((9 + M) * theta0))
        print ("TA = %7.2f" % TA, theta0, delta0)
        return TA

# Available thrust turbofan
        
def ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR):
        T, P, rho, a = atmosphere (hp, deltaT, RH);
        M = V / a
        theta0 = (T / 288.15) * (1 + ((1.4 - 1) / 2) * M**2)
        delta0 = (P / 101325) * (1 + ((1.4 - 1) / 2) * M**2) ** (1.4 / 0.4)
        if BPR <= 2:
                if theta0 <= TR:    
                        TA = 0.6 * Thstat * delta0
                else:
                        TA = 0.6  * Thstat * delta0 * (1 - 3.8 * (theta0 - TR) / theta0)
        else:
                if theta0 <= TR:
                        TA = Thstat * delta0 * (1 - 0.49 * M**0.5)
                else:
                        TA = Thstat * delta0 * (1 - 0.49 * M**0.5 - (3 * (theta0 - TR)) / (1.5 + M))
        print ("TA = %7.2f" % TA, "theta = %6.3f" % theta0, "delta0 = %6.3f" % delta0)
        return TA

# Available thrust turboprop

def ThrustTP (hp, deltaT, RH, V, Thstat, TR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        M = V / a;
        theta0 = (T / 288.15) * (1 + ((1.4 - 1) / 2) * M**2)
        delta0 = (P / 101325) * (1 + ((1.4 - 1) / 2) * M**2) ** (1.4 / 0.4)
        if M <= 0.1:
                TA = Thstat * delta0
        else:
                if theta0 <= TR:
                        TA = Thstat * delta0 * (1 - 0.96 * (M - 0.1)**0.25)
                else:
                        TA = Thstat * delta0 * (1 - 0.96 * (M - 0.1)**0.25 - 3 * (theta0 - TR) / (8.13 * (M - 0.1)))
        print ("TA = %7.2f" % TA)
        return TA

# Maximum speed turbojet
        
def  VmaxTJ (hp, deltaT, RH,  CDo, K, W, S, Thstat, TR, Dslope, Mdiv):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        V = VLDmax
        Delta = V
        while Delta > 0.5:
                M = V / a
                TA = ThrustTJ (hp, deltaT, RH, V, Thstat, TR)
                if M <= Mdiv:
                        Vmax = (( (TA/W) * (W/S) + (W/S) * ((TA/W)**2 - 4 * CDo * K)**0.5 ) / (rho * CDo))**0.5
                else:
                        Ddiv = 0.5 * rho * V**2 * S * (CDo + K * ( 2 * W / (rho * V**2 * S))**2)
                        slope = Dslope * Ddiv
                        Vmax = a * ((TA - Ddiv) / slope + Mdiv)
                Delta = abs( Vmax - V )
                V = Vmax
        print ("VmaxTJ = %4.2f" % V, Ddiv)
        return V

# Maximum speed turbofan

def VmaxTF (hp, deltaT, RH, CDo, K, W, S, Thstat, TR, BPR, Dslope, Mdiv):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        V = VLDmax
        Delta = V
        while Delta > 0.5:
                M = V / a
                TA = ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR)
                if M <= Mdiv:
                        Vmax = (( (TA/W) * (W/S) + (W/S) * ((TA/W)**2 - 4 * CDo * K)**0.5 ) / (rho * CDo))**0.5
                else:
                        Ddiv = 0.5 * rho * V**2 * S * (CDo + K * ( 2 * W / (rho * V**2 * S))**2)
                        slope = Dslope * Ddiv
                        Vmax = a * ((TA - Ddiv) / slope + Mdiv)
                Delta = abs( Vmax - V )
                V = Vmax
        print ("VmaxTF = %4.2f" % V)
        return V

# Maximum speed turboprop

def VmaxTP (hp, deltaT, RH, CDo, K, W, S, Thstat, TR, Dslope, Mdiv):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        V = VLDmax
        Delta = V
        while Delta > 0.5:
                M = V / a
                TA = ThrustTP (hp, deltaT, RH, V, Thstat, TR)
                if M <= Mdiv:
                        Vmax = (( (TA/W) * (W/S) + (W/S) * ((TA/W)**2 - 4 * CDo * K)**0.5 ) / (rho * CDo))**0.5
                        if (TA/W)*2 - 4 * CDo * K < 0:
                                Vmax = ( (TA/W) * (W/S) / (rho * CDo))**0.5
                        else:
                                Vmax = Vmax
                else:
                        Ddiv = 0.5 * rho * V**2 * S * (CDo + K * ( 2 * W / (rho * V**2 * S))**2)
                        slope = Dslope * Ddiv
                        Vmax = a * ((TA - Ddiv) / slope + Mdiv)
                Delta = abs( Vmax - V )
                V = Vmax - Delta * 0.5
        print ("VmaxTP = %4.2f" % V)
        return V

# Endurance turbojet
        
def EnduranceJet (hp, deltaT, RH, CDo, K, S, W1, W2, SFC):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        W = 0.5 * (W1 + W2)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        EJet = LDmax / (SFC * g) * log(W1/W2)
        print ("Endurance = %5.0f" % EJet)
        return EJet

# Fuel for Endurance turbojet 
        
def FuelEnduranceJet (hp, deltaT, RH, CDo, K, S, E, W2, SFC):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W2, S)
        W1 = W2 * math.exp ( E * SFC * g / LDmax)
        Wf = W1 - W2
        print ("W1 = %8.0f" % W1, "Wf = %8.0f" % Wf)
        return W1

# Fuel for Endurance turbojet 2
        
def FuelEnduranceJet2 (hp, deltaT, RH, CDo, K, S, E, W1, SFC):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W1, S)
        W2 = W1 * math.exp ( -E * SFC * g / LDmax)
        Wf = W1 - W2
        print ("W2 = %8.0f" % W2, "Wf = %8.0f" % Wf)
        return W2
    
# Endurance turboprop
        
def EnduranceProp (hp, deltaT, RH, CDo, K, W, S, W1, W2, SFCpr, etapr):
        W = 0.5 * (W1 + W2)
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        CL32CDmax,Potmin,VCLCD32max,CLPmin = Pmin (hp, deltaT, RH, CDo, K, W, S)
        EProp = etapr / SFCpr * (2 * S * rho / g**3)**0.5 * CL32CDmax * g**0.5  * ( W2**-0.5 - W1**-0.5 ) 
        print ("Endurance = %5.0f" % EProp)
        return EProp

# Maximum range turbojet
        
def MaxRangeTJ (hp, deltaT, RH, CDo, K, S, W1, W2, SFC):
        W = 0.5 * (W1 + W2)
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)  
        CL12CD = (3 / 4) * ( 1 / (3 * K * CDo**3))** 0.25
        Ramax = -2 * CL12CD / (SFC * g**0.5) * (2 / (rho * S))**0.5 * ( (W2 / g)**0.5 - (W1 / g)**0.5)
        print ("Range = %7.0f" % Ramax)
        return Ramax

# Maximum range turbofan
        
def MaxRangeTF (hp, deltaT, RH, CDo, K, S, W1, W2, SFC):
        W = 0.5 * (W1 + W2)
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)  
        CL12CD = (3 / 4) * ( 1 / (3 * K * CDo**3))** 0.25
        Ramax = -2 * CL12CD / (SFC * g**0.5) * (2 / (rho * S))**0.5 * ( (W2 / g)**0.5 - (W1 / g)**0.5)
        VCL12CD = ( 2 / rho * ( 3 * K / CDo ) ** 0.5 * ( W1 + W2 ) / (2 * S)) ** 0.5
        print ("Range = %7.0f" % Ramax, "W = %7.0f" % W, "CL12CD = %6.2f" % CL12CD, "VCL12CD = %4.2f" % VCL12CD)
        return Ramax

# Fuel for range turbofan
        
def FuelRangeTF (hp, deltaT, RH, CDo, K, S, Ra, W2, SFC):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        CL12CD = (3 / 4) * ( 1 / (3 * K * CDo**3))** 0.25
        W1 = g * ( Ra * SFC * g**0.5 / (2 * CL12CD)  * (rho * S / 2)**0.5 + (W2/g)**0.5)**2
        Wf = W1 - W2
        Ramax = -2 * CL12CD / (SFC * g**0.5) * (2 / (rho * S))**0.5 * ( (W2 / g)**0.5 - (W1 / g)**0.5)
        print ("W1 = %8.0f" % W1, "Wf = %7.0f" % Wf, "Range = %7.0f" % Ramax)
        return W1, Wf, CL12CD, Ramax
        
# Fuel for range turbofan2
        
def FuelRangeTF2 (hp, deltaT, RH, CDo, K, S, Ra, W1, SFC):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        CL12CD = (3 / 4) * ( 1 / (3 * K * CDo**3))** 0.25
        W2 = g * ( (W1/g)**0.5 - Ra * SFC * g**0.5 / (2 * CL12CD)  * (rho * S / 2)**0.5 )**2
        Wf = W1 - W2
        Ramax = -2 * CL12CD / (SFC * g**0.5) * (2 / (rho * S))**0.5 * ( (W2 / g)**0.5 - (W1 / g)**0.5)
        VCL12CD = ( 2 / rho * ( 3 * K / CDo ) ** 0.5 * ( W1 + W2 ) / (2 * S)) ** 0.5
        print ("W2 = %8.0f" % W2, "Wf = %7.0f" % Wf, "Range = %7.0f" % Ramax, "VCL12CD = %4.2f" % VCL12CD)
        return W2, Wf, CL12CD, Ramax, VCL12CD
        
# Maximum range turboprop

def MaxRangeTP (hp, deltaT, RH, CDo, K, S, W1, W2, SFCpr, etapr):
        W = 0.5 * (W1 + W2)
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)  
        Ramax = (etapr * LDmax) / (g * SFCpr) * log(W1 / W2)
        print ("Range = %7.0f" % Ramax)
        return Ramax

# Range at constant altitude and lift coefficient
        
def RangeJetHpCL (hp, deltaT, RH, CDo, K, W, S, W1, W2, SFC, V1):
        W = (W1 + W2) * 0.5;
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        RaHpCL = 2 * LDmax * V1 / (SFC * 9.807) * (1 - (W2 / W1)**0.5) 
        print ("Range = %7.0f" % RaHpCL)
        return RaHpCL

# Range at constan velocity and altitude

def RangeJetVHp (hp, deltaT, RH, CDo, K, W, S, W1, W2, SFC, V):
        W = (W1 + W2) * 0.5;
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        CL1 = W1 / (0.5 * rho * V**2 * S)
        CD1 = CDo + K * CL1**2
        LD1 = CL1 / CD1
        Wf = W1 - W2
        RaVHp = ( 2 * LDmax * V / (SFC * 9.807) ) * atan( (Wf/W1) * (LD1) / (2 * LDmax * (1 - K * CL1 * LD1 * Wf / W1))) 
        print ("Range = %7.0f" % RaVHp)
        return RaVHp

# Maxima tasa de viraje turbojet
        
def OmegamaxTJ(hp, deltaT, RH, W, S, K, CDo, Thstat, TR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)  
        V = VLDmax
        Delta = V
        while Delta > 0.5:
             TA = ThrustTJ (hp, deltaT, RH, V, Thstat, TR)
             VOmegamax = ( (W / S) * (2 / rho) * (K / CDo)**0.5)**0.5
             Delta = abs(VOmegamax - V)
             V = VOmegamax
        nOmegamax = ( (TA / W) * (1 / (K * CDo))**0.5 - 1)**0.5
        ROmegamax = VOmegamax**2 / (g * (nOmegamax**2 - 1)**0.5)
        print ("Vomegamax = %4.2f" % VOmegamax, "nOmegamax = %3.1f" % nOmegamax, "ROmegamax = %6.1f" % ROmegamax)
        return VOmegamax, nOmegamax, ROmegamax

# Maxima tasa de viraje turbofan
        
def OmegamaxTF(hp, deltaT, RH, W, S, K, CDo, Thstat, TR, BPR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)  
        V = VLDmax
        Delta = V
        while Delta > 0.5:
             TA = ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR)
             VOmegamax = ( (W / S) * (2 / rho) * (K / CDo)**0.5)**0.5
             Delta = abs(VOmegamax - V)
             V = VOmegamax
        nOmegamax = ( (TA / W) * (1 / (K * CDo))**0.5 - 1)**0.5
        ROmegamax = VOmegamax**2 / (g * (nOmegamax**2 - 1)**0.5)
        print ("Vomegamax = %4.2f" % VOmegamax, "nOmegamax = %3.1f" % nOmegamax, "ROmegamax = %6.1f" % ROmegamax)
        return VOmegamax, nOmegamax, ROmegamax

# Maxima tasa de viraje turboprop
        
def OmegamaxTP(hp, deltaT, RH, W, S, K, CDo, Thstat, TR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)  
        V = VLDmax
        Delta = V
        while Delta > 0.5:
             TA = ThrustTP (hp, deltaT, RH, V, Thstat, TR)
             VOmegamax = ( (W / S) * (2 / rho) * (K / CDo)**0.5)**0.5
             Delta = abs(VOmegamax - V)
             V = VOmegamax
        nOmegamax = ( (TA / W) * (1 / (K * CDo))**0.5 - 1)**0.5
        ROmegamax = VOmegamax**2 / (g * (nOmegamax**2 - 1)**0.5)
        print ("Vomegamax = %4.2f" % VOmegamax, "nOmegamax = %3.1f" % nOmegamax, "ROmegamax = %6.1f" % ROmegamax)
        return VOmegamax, nOmegamax, ROmegamax

# Minimo radio de viraje turbojet

def RminTJ(hp, deltaT, RH, W, S, K, CDo, Thstat, TR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S) 
        V = VLDmax
        Delta = V
        while Delta > 0.5:
            TA = ThrustTJ (hp, deltaT, RH, V, Thstat, TR)
            VRmin = ( 4 * K * W / (rho * (TA / W) * S))**0.5
            Delta = abs(VRmin - V)
            V = VRmin
        nRmin = ( 2 * (1 - (2 * K * CDo) / (TA / W)**2))**0.5
        Rmin = VRmin**2 / (g * (nRmin**2 - 1)**0.5)
        print ("VRmin = %4.2f" % VRmin, "nRmin = %3.1f" % nRmin, "Rmin = %6.1f" % Rmin)
        return VRmin, nRmin, Rmin

# Minimo radio de viraje turbofan

def RminTF(hp, deltaT, RH, W, S, K, CDo, Thstat, TR, BPR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S) 
        V = VLDmax
        Delta = V
        while Delta > 0.5:
            TA = ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR)
            VRmin = ( 4 * K * W / (rho * (TA / W) * S))**0.5
            Delta = abs(VRmin - V)
            V = VRmin
        nRmin = ( 2 * (1 - (2 * K * CDo) / (TA / W)**2))**0.5
        Rmin = VRmin**2 / (g * (nRmin**2 - 1)**0.5)
        print ("VRmin = %4.2f" % VRmin, "nRmin = %3.1f" % nRmin, "Rmin = %6.1f" % Rmin)
        return VRmin, nRmin, Rmin

# Minimo radio de viraje turboprop

def RminTP(hp, deltaT, RH, W, S, K, CDo, Thstat, TR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S) 
        V = VLDmax
        Delta = V
        while Delta > 0.5:
            TA = ThrustTP (hp, deltaT, RH, V, Thstat, TR)
            VRmin = ( 4 * K * W / (rho * (TA / W) * S))**0.5
            Delta = abs(VRmin - V)
            V = VRmin
        nRmin = ( 2 * (1 - (2 * K * CDo) / (TA / W)**2))**0.5
        Rmin = VRmin**2 / (g * (nRmin**2 - 1)**0.5)
        print ("VRmin = %4.2f" % VRmin, "nRmin = %3.1f" % nRmin, "Rmin = %6.1f" % Rmin)
        return VRmin, nRmin, Rmin

# Maximo angulo de ascenso turbojet

def ClimbThetaMaxTJ (hp, deltaT, RH, W, S, K, CDo, Thstat, TR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        V = VLDmax
        Delta = V
        while Delta > 0.5:
            TA = ThrustTJ (hp, deltaT, RH, V, Thstat, TR)
            thetamax = asin((TA / W) - (4 * CDo * K)**0.5)
            Vthetamax = ((2 / rho) * (K / CDo)**0.5 * (W / S) * cos(thetamax))**0.5
            Delta = abs(V - Vthetamax)
            V = Vthetamax
        RCthetamax = (Vthetamax * sin(thetamax))
        print ("ThetaMax = %4.2f" % thetamax, "VthetaMax = %4.2f" % Vthetamax, "RCThetaMax = %4.2f" % RCthetamax)
        return thetamax, Vthetamax, RCthetamax

# Maximo ángulo de ascenso turbofan

def ClimbThetaMaxTF (hp, deltaT, RH, W, S, K, CDo, Thstat, TR, BPR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        V = VLDmax
        Delta = V
        while Delta > 0.5:
            TA = ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR)
            thetamax = asin((TA / W) - (4 * CDo * K)**0.5)
            Vthetamax = ((2 / rho) * (K / CDo)**0.5 * (W / S) * cos(thetamax))**0.5
            Delta = abs(V - Vthetamax)
            V = Vthetamax
        RCthetamax = (Vthetamax * sin(thetamax))
        print ("ThetaMax = %4.2f" %thetamax, "VthetaMax = %4.2f" % Vthetamax, "RCThetaMax = %4.2f" % RCthetamax)
        return thetamax, Vthetamax, RCthetamax

# Maximo ángulo de ascenso turboprop

def ClimbThetaMaxTP (hp, deltaT, RH, W, S, K, CDo, Thstat, TR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        V = VLDmax
        Delta = V
        while Delta > 0.5:
            TA = ThrustTP (hp, deltaT, RH, V, Thstat, TR)
            thetamax = asin((TA / W) - (4 * CDo * K)**0.5)
            Vthetamax = ((2 / rho) * (K / CDo)**0.5 * (W / S) * cos(thetamax))**0.5
            Delta = abs(V - Vthetamax)
            V = Vthetamax
        RCthetamax = (Vthetamax * sin(thetamax))
        print ("ThetaMax = %4.2f" %thetamax, "VthetaMax = %4.2f" % Vthetamax, "RCThetaMax = %4.2f" % RCthetamax)
        return thetamax, Vthetamax, RCthetamax

# Maxima tasa de ascenso turbojet
        
def RCmaxTJ(hp, deltaT, RH, W, S, K, CDo, Thstat, TR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        V = VLDmax
        Delta = V;
        while Delta > 0.5:
            TA = ThrustTJ (hp, deltaT, RH, V, Thstat, TR)
            Z = 1 + (1 + 3 / (LDmax**2 * (TA / W)**2))**0.5
            VRCmax = ((TA * Z) / (3 * S * rho * CDo))**0.5
            Delta = abs(V - VRCmax)
            V = VRCmax
        RCmax = ((W/S) * Z / (3 * rho * CDo))**0.5 * (TA / W)**(3/2) * (1 - Z/6 - 3 / (2 * (TA / W)**2 * LDmax**2 * Z))
        thetaRCmax = asin(RCmax / VRCmax)
        print("VRCmax = %4.2f" % VRCmax, "RCmax = %3.2f" % RCmax, "ThetaRCmax = %3.2f" % thetaRCmax)
        return VRCmax, RCmax, thetaRCmax

# Maxima tasa de ascenso turbofan
        
def RCmaxTF(hp, deltaT, RH, W, S, K, CDo, Thstat, TR, BPR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        V = VLDmax
        Delta = V;
        while Delta > 0.5:
            TA = ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR)
            Z = 1 + (1 + 3 / (LDmax**2 * (TA / W)**2))**0.5
            VRCmax = ((TA * Z) / (3 * S * rho * CDo))**0.5
            Delta = abs(V - VRCmax)
            V = VRCmax
        RCmax = ((W/S) * Z / (3 * rho * CDo))**0.5 * (TA / W)**(3/2) * (1 - Z/6 - 3 / (2 * (TA / W)**2 * LDmax**2 * Z))
        thetaRCmax = asin(RCmax / VRCmax)
        print("VRCmax = %4.2f" % VRCmax, "RCmax = %3.2f" % RCmax, "ThetaRCmax = %3.2f" % thetaRCmax)
        return VRCmax, RCmax, thetaRCmax, Z

# Maxima tasa de ascenso turboprop
        
def RCmaxTP(hp, deltaT, RH, W, S, K, CDo, Thstat, TR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        V = VLDmax
        Delta = V;
        while Delta > 0.5:
            TA = ThrustTP (hp, deltaT, RH, V, Thstat, TR)
            Z = 1 + (1 + 3 / (LDmax**2 * (TA / W)**2))**0.5
            VRCmax = ((TA * Z) / (3 * S * rho * CDo))**0.5
            Delta = abs(V - VRCmax)
            V = VRCmax
        RCmax = ((W/S) * Z / (3 * rho * CDo))**0.5 * (TA / W)**(3/2) * (1 - Z/6 - 3 / (2 * (TA / W)**2 * LDmax**2 * Z))
        thetaRCmax = asin(RCmax / VRCmax)
        print("VRCmax = %4.2f" % VRCmax, "RCmax = %3.2f" % RCmax, "ThetaRCmax = %3.2f" % thetaRCmax)
        return VRCmax, RCmax, thetaRCmax

# Techo de servicio turbofan

def CeilingTF(deltaT, RH, W, S, K, CDo, Thstat, TR, BPR):
        hp = 0
        RC = 1
        while RC > 0.508:
            T, P, rho, a = atmosphere (hp, deltaT, RH)
            LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
            VRCmax, RCmax, thetaRCmax, Z = RCmaxTF (hp, deltaT, RH, W, S, K, CDo, Thstat, TR, BPR)
            rho = (W/S) * Z / (3 * CDo) * (1 / RCmax)**2 * (T / W)**3 * (1 - Z / 6 - 3 / ( (T / W)**2 * LDmax**2 * Z ) )**2
            hp = T0 / l * ( 1 - ( rho * R * T0 / P0 )**( l * R / (g - l * R) ) )
            RC = RCmax
        print (hp, RCmax)

# Time to climb - Turbojet

def TimeTCTJ(deltaT, RH, h1, h2, W, S, K, CDo, Thstat, TR):
        n = 10;
        Deltah = (h2 - h1) / n
        TimeTC = []
        for n in range(10):
            hp = (Deltah * n - Deltah / 2) + h1
            T, P, rho, a = atmosphere (hp, deltaT, RH)
            VRCmax, RCmax, thetaRCmax = RCmaxTJ(hp, deltaT, RH, W, S, K, CDo, Thstat, TR)
            Deltat = Deltah / RCmax
            TimeTC.append(Deltat)
        time = sum (TimeTC)
        print ("Time = %6.1f" % time, "sec")
        return time

# Time to climb - Turbofan

def TimeTCTF(deltaT, RH, h1, h2, W, S, K, CDo, Thstat, TR, BPR):
        n = 10;
        Deltah = (h2 - h1) / n
        TimeTC = []
        for n in range(10):
            hp = (Deltah * n - Deltah / 2) + h1
            T, P, rho, a = atmosphere (hp, deltaT, RH)
            VRCmax, RCmax, thetaRCmax, Z = RCmaxTF(hp, deltaT, RH, W, S, K, CDo, Thstat, TR, BPR)
            Deltat = Deltah / RCmax
            TimeTC.append(Deltat)
        time = sum (TimeTC)
        print ("Time = %6.1f" % time, "sec")
        return time

# Time to climb - Turboprop

def TimeTCTP(deltaT, RH, h1, h2, W, S, K, CDo, Thstat, TR):
        n = 10;
        Deltah = (h2 - h1) / n
        TimeTC = []
        for n in range(10):
            hp = (Deltah * n - Deltah / 2) + h1
            T, P, rho, a = atmosphere (hp, deltaT, RH)
            VRCmax, RCmax, thetaRCmax = RCmaxTP(hp, deltaT, RH, W, S, K, CDo, Thstat, TR)
            Deltat = Deltah / RCmax
            TimeTC.append(Deltat)
        time = sum (TimeTC)
        print ("Time = %6.1f" % time, "sec")
        return time        
    
# Best glide angle
        
def BestGlide (deltaT, RH, h1, h2, W, S, K, CDo):
        hp = (h1 + h2) / 2
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        LDmax,THmin,VLDmax, CLLDmax = MinThrust (hp, deltaT, RH, CDo, K, W, S)
        Thetamin = atan (1 / LDmax)
        ThetaminD = Thetamin * 180 / pi
        VThetamin = ( 2 * cos (Thetamin) * W / (rho * S) * (K / CDo)**0.5 )**0.5
        SRTmin = VThetamin * sin (Thetamin)
        print ("ThetaMin = %3.1f" % ThetaminD, "VThetaMin = %4.2f" % VThetamin, "SRThetnaMin = %3.2f" % SRTmin)
        return (Thetamin,VThetamin,SRTmin)

# Best sink rate

def BestSR (deltaT, RH, h1, h2, W, S, K, CDo):
		hp = (h1 + h2) / 2
		T, P, rho, a = atmosphere (hp, deltaT, RH)
		CL32CDmax,Potmin,VCLCD32max,CLPmin = Pmin (hp, deltaT, RH, CDo, K, W, S)
		SRmin = ( 2 * W / (rho * S))**0.5 * 1 / CL32CDmax
		V = VCLCD32max
		Delta = V
		while Delta > 0.5:
			ThetaSRmin = asin(SRmin / V)
			VSRmin = ( 2 * W * cos (ThetaSRmin) / (rho * S * CLPmin ))**0.5
			Delta = abs (V - VSRmin)
		print ( "ThetaSRmin = %3.1f" % ThetaSRmin, "VSRmin = %4.2f" % VSRmin, "SRmin = %3.2f" % SRmin)
		return (ThetaSRmin,VSRmin,SRmin)

# Takeoff performance (Kuc)
        
def TakeoffTF (hp, deltaT, RH, W, S, CLmax, CDo, K, FlapsMax, Flaps, CLroll, Dtroll, hOB, mu, hMAC, b, Thstat, TR, BPR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        Kuc = (-2.65 / FlapsMax * Flaps + 5.81) * 10**-5 
        DCDLG = W / S * Kuc * (W/g)**-0.215
        G = (16 * hMAC / b)**2 / ( 1 + (16 * hMAC / b)**2)
        Vi = 0
        n = 10
        Dist = []
        Vs = Vstall (hp, deltaT, RH, W, S, CLmax)
        Vlo = 1.1 * Vs
        print (Vlo)
        DeltaV = (Vlo - Vi)/n
        print (DeltaV)
        for r in range(n):
            V = DeltaV * (r + 1) - DeltaV/2
            TA = ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR)
            CD = CDo + DCDLG + (K / 3 + G * K) * CLroll**2
            D = 0.5 * rho * S * V**2 * CD
            Ffr = mu * (W - 0.5 * rho * S * V**2 * CLroll)
            Ftot = TA - D - Ffr
            Dtime = DeltaV * (W / g) / Ftot
            Dist.append(V * Dtime)
        Sg = sum (Dist)
        Sr = Dtroll * Vlo
        R = (1.15 * Vs)**2 / (g * 0.19)
        thetaTO = acos(1 - hOB / R)
        Sa = R * sin (thetaTO)
        STO = Sg + Sr + Sa
        print ("Sg = %4.1f" % Sg, "Sr = %3.1f" % Sr, "R = %4.1f" % R, "Sa = %3.1f" % Sa, "Takeoff distance = %4.1f" % STO)
        return (Sg, Sr, Sa, STO)

# Takeoff performance (with CL and CD)
        
def TakeoffTF2 (hp, deltaT, RH, W, S, CLmax, CD, CLroll, Dtroll, hOB, mu, Thstat, TR, BPR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        Vi = 0
        n = 10
        Dist = []
        Vs = Vstall (hp, deltaT, RH, W, S, CLmax)
        Vlo = 1.1 * Vs
        print (Vlo)
        DeltaV = (Vlo - Vi)/n
        for r in range(n):
            V = DeltaV * (r + 1) - DeltaV/2
            TA = ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR)
            D = 0.5 * rho * S * V**2 * CD
            Ffr = mu * (W - 0.5 * rho * S * V**2 * CLroll)
            Ftot = TA - D - Ffr
            Dtime = DeltaV * (W / g) / Ftot
            Dist.append(V * Dtime)
        Sg = sum (Dist)
        Sr = Dtroll * Vlo
        R = (1.15 * Vs)**2 / (g * 0.19)
        thetaTO = acos(1 - hOB / R)
        Sa = R * sin (thetaTO)
        STO = Sg + Sr + Sa
        print ("Sg = %4.1f" % Sg, "Sr = %3.1f" % Sr, "R = %4.1f" % R, "Sa = %3.1f" % Sa, "Takeoff distance = %4.1f" % STO)
        return (Sg, Sr, Sa, STO)

       
# Landing performance (Kuc)
        
def LandingTF (hp, deltaT, RH, W, S, CLmax, CDo, K, FlapsMax, Flaps, CLroll, Dtdelay, adelay, hOB, theta, mu, hMAC, b, Thstat, Rev, TR, BPR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        Kuc = (-2.65 / FlapsMax * Flaps + 5.81) * 10**-5 
        DCDLG = W / S * Kuc * (W/g)**-0.215
        G = (16 * hMAC / b)**2 / ( 1 + (16 * hMAC / b)**2)
        Vf = 0
        n = 10
        Dist = []
        Vs = Vstall (hp, deltaT, RH, W, S, CLmax)
        Vflare = 1.23 * Vs
        R = Vflare **2 / (0.2 * g)
        hf = R * (1 - cos( theta * pi / 180))
        Sa = (hOB - hf) / (tan (theta))
        Sf = R * sin(theta)
        VTD = 1.15 * Vs
        GS = VTD - (0.5 * adelay * Dtdelay)
        Sdelay = Dtdelay * GS
        Vfb = 2 * GS - VTD
        DeltaV = (Vfb - Vf)/n
        print (DeltaV)
        for r in range(n):
            V = DeltaV * (r + 1) - DeltaV/2
            TA = ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR)
            CD = CDo + DCDLG + (K / 3 + G * K) * CLroll**2
            D = 0.5 * rho * S * V**2 * CD
            Ffr = mu * (W - 0.5 * rho * S * V**2 * CLroll)
            Ftot = -( TA * Rev ) - D - Ffr
            Dtime = DeltaV * (W / g) / Ftot
            Dist.append(V * Dtime)
        Sg = sum (Dist)
        SLN = Sg + Sdelay + Sf + Sa
        print ("Sg = %4.1f" % Sg, "Sdelay = %3.1f" % Sdelay, "R = %4.1f" % R, "Sf = %3.1f" % Sf, "Sa = %3.1f" % Sa, "Landing distance = %4.1f" % SLN)
        return (Sg, Sdelay, Sf, Sa)

# Landing performance (with CL and CD)
        
def LandingTF2 (hp, deltaT, RH, W, S, CLmax, CD, CLroll, Dtdelay, adelay, hOB, theta, mu, Thstat, Rev, TR, BPR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        Vf = 0
        n = 10
        Dist = []
        Vs = Vstall (hp, deltaT, RH, W, S, CLmax)
        Vflare = 1.23 * Vs
        R = Vflare **2 / (0.2 * g)
        hf = R * (1 - cos( theta * pi / 180))
        Sa = (hOB - hf) / tan (theta * pi /180)
        Sf = R * sin(theta)
        VTD = 1.15 * Vs
        GS = VTD - (0.5 * adelay * Dtdelay)
        Sdelay = Dtdelay * GS
        Vfb = 2 * GS - VTD
        DeltaV = (Vfb - Vf)/n
        print (DeltaV)
        for r in range(n):
            V = DeltaV * (r + 1) - DeltaV/2
            TA = ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR)
            D = 0.5 * rho * S * V**2 * CD
            Ffr = mu * (W - 0.5 * rho * S * V**2 * CLroll)
            Ftot = -( TA * Rev ) - D - Ffr
            Dtime = - DeltaV * (W / g) / Ftot
            print (Dtime)
            Dist.append(V * Dtime)
        Sg = sum (Dist)
        SLN = Sg + Sdelay + Sf + Sa
        print ("Sg = %4.1f" % Sg, "Sdelay = %3.1f" % Sdelay, "R = %4.1f" % R, "Sf = %3.1f" % Sf, "Sa = %3.1f" % Sa, "Landing distance = %4.1f" % SLN)
        return (Sg, Sdelay, Sf, Sa)
    
# Takeoff performance (with CL and CD)
        
def TakeoffTF2a (hp, deltaT, RH, W, S, CLmax, CD, CLroll, Dtroll, hOB, mu, Thstat, TR, BPR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        Vi = 0
        n = 10
        Dist = []
        Vs = Vstall (hp, deltaT, RH, W, S, CLmax)
        Vlo = 77.27
        print (Vlo)
        DeltaV = (Vlo - Vi)/n
        for r in range(n):
            V = DeltaV * (r + 1) - DeltaV/2
            TA = ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR)
            D = 0.5 * rho * S * V**2 * CD
            Ffr = mu * (W - 0.5 * rho * S * V**2 * CLroll)
            Ftot = TA - D - Ffr
            Dtime = DeltaV * (W / g) / Ftot
            Dist.append(V * Dtime)
        Sg = sum (Dist)
        Sr = Dtroll * Vlo
        R = (1.15 * Vs)**2 / (g * 0.19)
        thetaTO = acos(1 - hOB / R)
        Sa = R * sin (thetaTO)
        STO = Sg + Sr + Sa
        print ("Sg = %4.1f" % Sg, "Sr = %3.1f" % Sr, "R = %4.1f" % R, "Sa = %3.1f" % Sa, "Takeoff distance = %4.1f" % STO)
        return (Sg, Sr, Sa, STO)
    
def LandingTF2a (hp, deltaT, RH, W, S, CLmax, CD, CLroll, Dtdelay, adelay, hOB, theta, mu, Thstat, Rev, TR, BPR):
        T, P, rho, a = atmosphere (hp, deltaT, RH)
        Vf = 0
        n = 10
        Dist = []
        Vs = Vstall (hp, deltaT, RH, W, S, CLmax)
        Vflare = 1.23 * Vs
        R = Vflare **2 / (0.2 * g)
        hf = R * (1 - cos( theta * pi / 180))
        Sa = (hOB - hf) / tan (theta * pi /180)
        Sf = R * sin(theta)
        VTD = 1.15 * Vs
        GS = VTD - (0.5 * adelay * Dtdelay)
        Sdelay = Dtdelay * GS
        Vfb = 1.03 * Vs
        vfb = 82.9
        DeltaV = (Vfb - Vf)/n
        print (DeltaV)
        for r in range(n):
            V = DeltaV * (r + 1) - DeltaV/2
            TA = ThrustTF (hp, deltaT, RH, V, Thstat, TR, BPR)
            D = 0.5 * rho * S * V**2 * CD
            Ffr = mu * (W - 0.5 * rho * S * V**2 * CLroll)
            Ftot = -( TA * Rev ) - D - Ffr
            Dtime = - DeltaV * (W / g) / Ftot
            print (Dtime)
            Dist.append(V * Dtime)
        Sg = sum (Dist)
        SLN = Sg + Sdelay + Sf + Sa
        print ("Sg = %4.1f" % Sg, "Sdelay = %3.1f" % Sdelay, "R = %4.1f" % R, "Sf = %3.1f" % Sf, "Sa = %3.1f" % Sa, "Landing distance = %4.1f" % SLN)
        return (Sg, Sdelay, Sf, Sa)
    