# Opendomain
Opendomain is the Python Script intended to open selected domains from files into Browser. Opening Selected specific Domains via line Number from a large file with domains into your favorite Browser. During Performing a Information Gathering during Security Assessment, we usually discovered and enumerate large quantity of Sub-domain and Adjust / Sort them into the File. Defacto tools like [Crt](https://crt.sh), [Sublister](https://github.com/aboul3la/Sublist3r),[FDNS](https://www.google.com/search?client=firefox-b-d&q=rapid+7+dns), [shodan](https://shodan.io)  enumerate subdomain and provide list of domain as output to the user.Furthermore, it requires us to open some of the domain in Browser and Analyzing the content of Domain to Perform Security Assessment. While Opening this domains from file, it is a Tedious/Consuming to copying these Domain Manually from file and pasting them in the Browser. Hence, some degree of Automation can assist us to open this domains (selected by user) from file and open into the Browser. Opendomain exactly performs this function. Currently, opendomain performs two sets of function :

[1.Opening specific individual domain from file]( https://github.com/Roshan-Poudel/opendomain/blob/main/README.md#to-open-individual-domain )

[2. Opening multiple domains from file within the range](https://github.com/Roshan-Poudel/opendomain#to-open-multiple-domains-at-once)

# Sample File with list of domain
Lets assume following as sample list of domains:

<img src="https://github.com/Roshan-Poudel/images/blob/master/subdomain.jpg">  

# To open individual domain
*Syntax: python domain.txt <line_number_of_domain>*
### TO open domain ```https://site.com ``` from the above [File](https://github.com/Roshan-Poudel/opendomain/blob/main/README.md#sample-file-with-list-of-domain) into Browser provide its corresponding line Number as Argument
```
python domain.txt 1
```
## The domain opens in Firefox
<img src="https://github.com/Roshan-Poudel/images/blob/master/opening.png">

# To open Multiple Domains at Once
*Syntax: python domain.txt <line_number_of_domain>*

### To open the domain range ```https://site.com``` to ```https://developers.site.com``` provide the Initiating and Ending Line of Domain 
```
python domain.txt 1 4
```
##  Output: All the domains between line number 1 and 4 opens in Firefox
 
