#Truss optimization program
import math
P = float (input ("Please enter the max force in N: "))
Distance = float (input ("Please enter the distance between two joint in mm: "))
B = Distance / 2
E = 210000 #Young's modulus in MPa
Syield = 400 # Yield stress in MPa
Result = 10000000
for d in range (20,100):
    for t_f in range (5,90):
        for H in range (500,1500):
            t=t_f/10
            I = math.pi*t*d*(d**2+t**2)/8 #second moment of inertia
            F = P * math.sqrt(math.pow(B,2)+math.pow(H,2))/H/2 # member force
            A = math.pi*t*d # Bar area
            S = F / A # Member stress
            L = math.sqrt(math.pow(H,2)+math.pow(B,2))
            Sbuckling = math.pow(math.pi,2)*E*I/math.pow(L,2)/A #Buckling stress
            V =2*A*L #Bar volume
            fobj = 2*d*t*math.pi*math.sqrt(math.pow(H,2)+math.pow(B,2)) #objective function definition
            g1 = (P*math.sqrt(math.pow(H,2)+math.pow(B,2))/2/H/d/t/math.pi) - Syield
            g2 = (P*math.sqrt(math.pow(H,2)+math.pow(B,2))/2/H/d/t/math.pi) - (math.pow(math.pi,2)*E*(math.pow(d,2)+math.pow(t,2))/8/(math.pow(H,2)+math.pow(B,2)))
            if g1<=0 and g2<=0:
                if fobj < Result:
                    Result = fobj
                    Diameter = d
                    Height = H
                    Thickness = t
                    Weight = fobj*0.000000001*7895.0
print ("Weight is", Weight)
print ("Diameter is", Diameter)
print ("Height is", Height)
print ("Thickness is", Thickness)
