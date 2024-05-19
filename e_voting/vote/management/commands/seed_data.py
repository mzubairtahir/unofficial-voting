from typing import Any
from django.core.management.base import BaseCommand
from vote.models import Party


class Command(BaseCommand):
    help = "Command to seed initial data in database    "

    

    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("seeding data...")
        data = {
                "name": [
                    "Pakistan Tehreek-e-Insaf",
                    "Pakistan Muslim League-Nawaz",
                    "Pakistan Peoples Party",
                    "Jamaat-e-Islami",
                    "Jamiat Ulema-e-Islam (F)",
                    "Tehreek-e-Labbaik Pakistan",
                    "Awami National Party",
                    "Muttahida Qaumi Movement",
                    "Balochistan Awami Party",
                    "Pakhtunkhwa Milli Awami Party"
                ],
                "code": [
                    "PTI",
                    "PML-N",
                    "PPP",
                    "JI",
                    "JUI-F",
                    "TLP",
                    "ANP",
                    "MQM",
                    "BAP",
                    "PkMAP"
                ],

                "image": [
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Flag_of_the_Pakistan_Tehreek-e-Insaf.svg/2560px-Flag_of_the_Pakistan_Tehreek-e-Insaf.svg.png",
                        "https://upload.wikimedia.org/wikipedia/commons/d/d9/PMLN_2021_Flag.png", 
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Flag_of_Pakistan_Peoples_Party.PNG/640px-Flag_of_Pakistan_Peoples_Party.PNG",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Jamaat-e-Islami_Pakistan_Flag.svg/1200px-Jamaat-e-Islami_Pakistan_Flag.svg.png",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Flag_of_JUI.svg/1280px-Flag_of_JUI.svg.png",
                        "https://upload.wikimedia.org/wikipedia/commons/d/da/TLP_Flag.png",
                        "https://upload.wikimedia.org/wikipedia/commons/c/cb/Awami_National_Party_flag.png",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/MQM_Flag.png/640px-MQM_Flag.png",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Balochistan_Awami_Party_flag.png/150px-Balochistan_Awami_Party_flag.png",
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/PKMAP_flag.PNG/150px-PKMAP_flag.PNG"

                          ]
            }
        

        rows_to_create = []

        n = len(data['name'])
        for i in range(n):
            name = data['name'][i]
            code = data['code'][i]
            image = data['image'][i]
            rows_to_create.append(Party(name=name, picture = image, code = code))
        
        Party.objects.bulk_create(rows_to_create)
        self.stdout.write("Data added")




            
        