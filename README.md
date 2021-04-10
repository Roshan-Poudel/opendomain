# Opendomain
Opening Selected specific domains via line Number from a large file with domains into your favorite browser. During Performing a Information Gathering during Security Assessment, we usually discovered and enumerate large quantity of Sub-domain and Adjust/Sort them into the File. While Opening this domains from file it is a Tedious/Consuming to copying these domain from file and pasting them in the Browser. Hence, some degree of Automation can assist us to open this domains (selected by user) from file and open into the Browser. Opendomain exactly performs this function. Currently,  

# Sample File with list of domain
<img src="https://github.com/Roshan-Poudel/images/blob/master/subdomain.jpg">  

# To open individual domain
*Syntax: python domain.txt <line_number_of_domain>*
### TO open ```https://site.com ``` from the above File provide its corresponding line Number
```
python domain.txt 1
```
## The domain opens in Firefox
<img src="https://github.com/Roshan-Poudel/images/blob/master/opening.png">

# To open Multiple Domains at Once
*Syntax: python domain.txt <line_number_of_domain>*

```
python domain.txt start_of_domain end_of_domain
```
### To open the domain range ```https://site.com``` to ```https://developers.site.com``` provide the Initiating and Ending Line of Domain 
```
python domain.txt 1 4
```
##  Output: All the domains between line number 1 and 4 opens in Firefox
