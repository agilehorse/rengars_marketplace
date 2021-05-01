class TestDataGenerator:
    @staticmethod
    def get_job_offer():
        return {
            "companyName": "FitWolfe",
            "description": "We are looking for a fellow developer that can help us build the greatest online fitness training",
            "id": 1,
            "positionName": "FullStack Java React Developer",
            "poster": {
                "birthDate": "1990-04-25",
                "email": "dmbulko@gmail.com",
                "phoneNumber": "+420 608 801 031",
                "id": 7
            }
        }

    @staticmethod
    def get_create_job_offer_dto():
        return {
            "companyName": "FitWolfe",
            "description": "We are looking for a fellow developer that can help us build the greatest online fitness "
                           "training",
            "id": 1,
            "positionName": "FullStack Java React Developer",
            "posterId": 7
        }

    @staticmethod
    def get_job_application():
        return {
            "applicant": {
                "birthDate": "2000-04-25",
                "email": "best.developer@ever.com",
                "id": 5,
                "phoneNumber": "+420 420 420 420"
            },
            "jobOfferId": 6,
            "note": "Hello I have 3 years experience. Please give me work or I will starve to death.",
            "state": "NEW"
        }

    @staticmethod
    def get_create_job_application_dto(job_offer_id=6):
        return {
            "applicantId": 5,
            "jobOfferId": job_offer_id,
            "note": "Hello I have 3 years experience. Please give me work or I will starve to death.",
            "state": "NEW"
        }
