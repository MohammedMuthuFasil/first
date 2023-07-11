import difflib

def autocorrect(word, dictionary, threshold):
    if word in dictionary:
        return word

    closest_word = difflib.get_close_matches(word, dictionary, n=1, cutoff=threshold)
    if closest_word:
        return closest_word[0]
    else:
        return word

# Example usage

word_dictionary =['Natural', 'Asian Paints', 'Industries Ltd', 
                  ' (ONGC) Power Grid Corporation of India Ltd', 'Products', 'Company', 
                  ' Bajaj Auto Ltd', ' Bharat Petroleum Corporation Ltd',
                  ' Nestle India Ltd', 'and', 'Mahindra', 'Maruti',
                  'Petroleum', '(M&M)', 'Finance Corporation Ltd', 
                  ' Bharat Petroleum ', 'State', '&',
                  'Suzuki', ' HDFC Life', ' HDFC Bank Ltd', 'Ltd',
                  'Corporation', 'Coal', 'Laboratories', 'Ltd.', ' Indian Oil Corporation Ltd',
                  'Life', 'Hero', 'and Special ', ' IndusInd Bank Ltd', 'Pharmaceutical',
                  ' Kotak Mahindra Bank Ltd', 'Services', 'Motors', 'Bank', 'UPL', 
                  ' Tata Steel Ltd', ' Bajaj Finserv Ltd', 'Economic', ' Ltd',
                  ' Oil and Natural Gas Corporation Ltd', 'Ltd.Adani Ports ', 
                  ' NTPC Ltd', 'Cipla', 'Consumer',
                  ' Housing Development Finance Corporation Ltd', ' Titan Company Ltd',
                  '(SBI)', 'Nestle', ' Infosys Ltd', '(ONGC)', ' Bajaj ', ' Shree Cement Ltd',
                  'Hindalco', ' Wipro LtdAdani Ports and Special Economic Zone Ltd', 'Hindustan',
                  'Reliance', " Divi's Laboratories Ltd", 'Economic Zone Ltd', 'Power',
                  '(L&T) Mahindra & Mahindra Ltd', 'Oil', ' Asian Paints Ltd', 'Steel',
                  ' ITC Ltd', 'Industries', ' State Bank of India (SBI) Sun Pharmaceutical Industries Ltd',
                  'Zone', ' Bajaj Finance Ltd', ' Hindalco ', 'tata motors', ' Cipla Ltd',
                  ' UltraTech Cement Ltd', "Divi's", ' Grasim Industries Ltd', 'Auto',
                  ' Bajaj Auto ', ' Eicher Motors Ltd', 'ITC', '(TCS)', 'Paints', ' UPL Ltd', 
                  'Adani Ports', ' (HDFC) ICICI Bank Ltd', 'Airtel', ' Finserv Ltd',
                  ' Larsen & Toubro Ltd', ' Hindalco Industries Ltd', ' Hero MotoCorp Ltd', 
                  ' (TCS) Tata Motors Ltd', ' Bharti Airtel Ltd', "Reddy's", 'UltraTech', 'Cement',
                  'Bharti', ' Britannia Industries Ltd', ' Axis Bank', 'Tata', ' JSW Steel Ltd',
                  'Special', ' HCL Technologies Ltd', 'Technologies', ' SBI Life Insurance Company Ltd',
                  'Britannia', ' ICICI Bank Ltd', 'ICICI', 'Grasim', 'MotoCorp', 'JSW', 'Housing',
                  ' Dr', 'Asian', ' Tata Consumer Products Ltd', ' HDFC Life Insurance Company Ltd', 
                  ' Reliance Industries Ltd', '(L&T)', 'Finance Ltd', 'Corporation Ltd', 'Bajaj',
                  " Divi's Laboratories", 'Grid', ' Coal India Ltd', 'Toubro', ' Wipro Ltd', 'Axis', 'Unilever', '(HDFC)', ' Hindustan Unilever Ltd', 'Larsen', 'Tech', 'Kotak', 'Wipro', 
                  ' Housing Development ', 'Shree', ' Indian Oil Corporation', ' Bajaj', 'Dr.', 'Indian', 
                  ' (M&M) Maruti Suzuki India Ltd', 'HDFC', ' Tata Consultancy Services Ltd', 
                  ' Bharti Airtel', 'Consultancy', 'Gas', 'NTPC', 'Finance', 'India', 'Titan', 'Insurance', 'Finserv', 'of', 
                  " Reddy's Laboratories Ltd", ' Insurance Company Ltd', 'Bharat', 
                  'Eicher', ' Axis Bank Ltd', ' Tech Mahindra Ltd', 'SBI', 'HCL', 'Development', 'Infosys', 'IndusInd', 'Sun']
similarity_threshold = 0.4

corrected_word = autocorrect('taaaa', word_dictionary, similarity_threshold)
print(corrected_word)  

