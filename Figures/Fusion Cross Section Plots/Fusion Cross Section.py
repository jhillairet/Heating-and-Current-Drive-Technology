# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 15:27:56 2015

@author: JH218595
"""

from pylab import *

""" 
Plot the Reaction rates in cm^3 s^-1 as a function of
 E, the energy in keV of the incident particle 
 [the first ion of the reaction label]

 Data taken from NRL Formulary 2013.
"""
E,DD,DT,DH=loadtxt('reaction_rates_vs_energy_incident_particle.txt', 
                   skiprows=1, unpack=True)

figure(num=1)
clf()
loglog(E, DD, E, DT, E, DH, lw=2)
grid()
xlabel('Temperature [keV]', fontsize=16)
ylabel('Reaction Rates $<\sigma v>$ [$cm^3.s^{-1}$]', fontsize=16)
xticks(fontsize=14)
yticks(fontsize=14)
ylim([1e-26, 2e-15])
legend(('D-D', 'D-T', 'D-He$^3$'), loc='best', fontsize=18)

"""
Plot the total cross section in m^2 for various species vs incident energy in keV

"""

def cross_section(E, A):
    """
    The total cross section in barns (1 barns=1e-24 cm^2) as a function of E, 
    the energy in keV of the incident particle.
    
    Formula from NRL Formulary 2013.
    """
    sigma_T = (A[4]+((A[3]-A[2]*E)**2+1)**(-1) * A[1])/(E*(exp(A[0]/sqrt(E))-1))
    return(sigma_T)
    
A_DD_a = [46.097, 372, 4.36e-4, 1.220, 0]
A_DD_b = [47.88, 482, 3.08e-4, 1.177, 0]
A_DT   = [45.95, 50200, 1.368e-2, 1.076, 409]
A_DHe3 = [89.27, 25900, 3.98e-3, 1.297, 647]
A_TT   = [38.39, 448, 1.02e-3, 2.09, 0]
A_THe3 = [123.1, 11250, 0, 0, 0]

E = logspace(0, 3, 501)
barns2SI = 1e-24 * 1e-4 # in m^2

sigma_DD = barns2SI*(cross_section(E, A_DD_a) + cross_section(E, A_DD_b))
sigma_DT = barns2SI*cross_section(E, A_DT)
sigma_DHe3 = barns2SI*cross_section(E, A_DHe3)

figure(num=2)
clf()
loglog(E, sigma_DD, E, sigma_DT, E, sigma_DHe3, lw=2)
grid()
xlabel('Deuteron Energy [keV]', fontsize=16)
ylabel('Cross-section $\sigma$ [$m^2$]', fontsize=16)
legend(('D-D', 'D-T', 'D-He$^3$'), loc='best', fontsize=18)
ylim([1e-32, 2e-27])
xticks(fontsize=14)
yticks(fontsize=14)
