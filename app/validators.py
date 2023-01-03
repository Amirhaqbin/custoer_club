from django.core.validators import RegexValidator


mobile_phone_regex = RegexValidator(  
                                    regex=r'^09(1[0-9]|3[0-9])[0-9]{7}$', 
                                    message="mobile phone number must be in this format '09123456789' and exactly 11 digits."
                                )

telephone_regex = RegexValidator(  
                                    regex=r'^([0-9]{3})?[0-9]{8}$', 
                                    message="telephone number must be either 8 or 11 digits."
                                )

id_number_regex = RegexValidator(  
                                    regex=r'^\d{10}$', 
                                    message="id number must be 10 digits exactly."
                                )
zip_code_regex = RegexValidator(  
                                    regex=r'^\d{10}$', 
                                    message="zip code must be 10 digits exactly."
                                )