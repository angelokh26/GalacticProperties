''' Created by Angelo Hollett (angelokh26@gmail.com) - 2019-10-19 12:55:00

This program is used to produce 1D and 2D histogram plots to deduce trends 
between various properties of galaxies from SDSS DR8.'''

import astropy
import matplotlib.pyplot as plt
import numpy as np

from astropy.table import Table
from astropy.io import fits


#-----------------Open the fits file--------------------#
fits = fits.open('galSpecExtra-dr8.fits')
data = Table.read(fits[1], format='fits')
#-------------------------------------------------------#

#----------------Read in data to arrays-----------------#
mass = data['LGM_TOT_P50']
metal = data['OH_P50']
star_form = data['SFR_TOT_P50']
#-------------------------------------------------------#

#empty arrays, used later...
arr_mass=[]           
arr_metal=[]
arr_star_form=[]

cutoff=-9999

# accept only values in a sensible range
for i in range(0,len(metal)):
    if mass[i]>0 and metal[i]>cutoff and star_form[i]>cutoff:
        arr_mass.append(mass[i])
        arr_metal.append(metal[i])
        arr_star_form.append(star_form[i])

#---------------------------Plot the first histogram, mass v number-----------------------------#
plt.figure(figsize=(10,8))        
plt.hist(arr_mass, color='#eb9113', label = 'Mass Distribution')
plt.title('Mass Distribution of Galaxies (SDSS Dr8)')
plt.xlabel('log(M_tot/M_sol)')
plt.ylabel('Number of Galaxies')

#-----Compute the 10th and 90th percentiles, print the values, and plot the vertical lines------#
mass_10_perc = np.percentile(arr_mass, 10)
print ('----------------------------------------------------')
print ('The 10th percentile of mass is: ')
print (mass_10_perc)
print ('----------------------------------------------------')
plt.axvline(x=mass_10_perc, c='#9c18de', ls='--', label='10th percentile')


mass_90_perc = np.percentile(arr_mass, 90)
plt.axvline(x=mass_90_perc, c='#10b028', ls='--', label='90th percentile')
plt.legend(loc='best')
print ('----------------------------------------------------')
print ('The 90th percentile of mass is: ')
print (mass_90_perc)
print ('----------------------------------------------------')
plt.savefig('hist_mass.png', dpi=600, bbox_inches='tight')

#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#


#-------------------------Plot the second histogram, metal v number-----------------------------#
plt.figure(figsize=(10,8))
plt.hist(arr_metal, color='#eb9113', label = 'Metallicity Distribution')
plt.title('Metallicity Distribution of Galaxies (SDSS Dr8)')
plt.xlabel('Metallicity (12 + log(O/H))')
plt.ylabel('Number of Galaxies')

#-----Compute the 10th and 90th percentiles, print the values, and plot the vertical lines------#
metal_10_perc = np.percentile(arr_metal, 10)
plt.axvline(x=metal_10_perc, c='#9c18de', ls='--', label='10th percentile')
print ('----------------------------------------------------')
print ('The 10th percentile of metallicity is: ')
print (metal_10_perc)
print ('----------------------------------------------------')
metal_90_perc = np.percentile(arr_metal, 90)

plt.axvline(x=metal_90_perc, c='#10b028', ls='--', label='90th percentile')
print ('----------------------------------------------------')
print ('The 90th percentile of metallicity is: ')
print (metal_90_perc)
print ('----------------------------------------------------')
plt.legend(loc='best')
plt.savefig('hist_metallicity.png', dpi=600, bbox_inches='tight')

#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#

#---------------------Plot the third histogram, star formation v number-------------------------#
plt.figure(figsize=(10,8))
plt.hist(arr_star_form, color='#eb9113', label = 'Star Formation Rate Distribution')
plt.title('Star Formation Rate Distribution of Galaxies (SDSS dr8)')
plt.xlabel('Star Formation Rate (SFR/log(M_sol/yr))')
plt.ylabel('Number of Galaxies')

#-----Compute the 10th and 90th percentiles, print the values, and plot the vertical lines------#
star_form_10_perc = np.percentile(arr_star_form, 10)
plt.axvline(x=star_form_10_perc, c='#9c18de', ls='--', label='10th percentile')
print ('----------------------------------------------------')
print ('The 10th percentile of star formation rate is: ')
print (star_form_10_perc)
print ('----------------------------------------------------')
star_form_90_perc = np.percentile(arr_star_form, 90)

plt.axvline(x=star_form_90_perc, c='#10b028', ls='--', label='90th percentile')
print ('----------------------------------------------------')
print ('The 90th percentile of star formation rate is: ')
print (star_form_90_perc)
print ('----------------------------------------------------')
plt.legend(loc='best')
plt.savefig('hist_star_form.png', dpi=600, bbox_inches='tight')

#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#

#---------------Create a 2d histogram for metal & mass-------------#
plt.figure(figsize=(12,8))
plt.hist2d(arr_metal, arr_mass, bins=[40,40], cmap='viridis')
plt.title('Correlation of Galactic Metallicity with Mass')
plt.xlabel('Metallicity (12 + log(O/H))')
plt.ylabel('log(M_tot/M_sol)')
plt.colorbar()
plt.savefig('Metal_Mass_correlation.png', dpi=600, bbox_inches='tight')
#------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#

#-------Create a 2d histogram for metal and star formation---------#
plt.figure(figsize=(12,8))
plt.hist2d(arr_metal, arr_star_form, bins=[40,40], cmap='viridis')
plt.title('Correlation of Galactic Metallicity with Star Formation Rate')
plt.xlabel('Metallicity (12 + log(O/H))')
plt.ylabel('Star Formation Rate (SFR/log(M_sol/yr))')
plt.colorbar()
plt.savefig('Metal_starformation_correlation.png', dpi=600, bbox_inches='tight')
#------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#

#fits.close()