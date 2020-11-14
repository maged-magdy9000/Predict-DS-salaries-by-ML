from flask import Flask, render_template, request
import joblib



app = Flask(__name__)

model = joblib.load('Model_deplo.pkl')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    is_title_0 = 1 if request.form['job title'] == 'job_simp_data scientist' else 0
    is_title_1 = 1 if request.form['job title'] == 'job_simp_data engineer' else 0
    is_title_2 = 1 if request.form['job title'] == 'job_simp_director' else 0
    is_title_3 = 1 if request.form['job title'] == 'job_simp_analyst' else 0
    is_title_4 = 1 if request.form['job title'] == 'job_simp_manager' else 0
    is_title_5 = 1 if request.form['job title'] == 'job_simp_ml' else 0
    is_title_6 = 1 if request.form['job title'] == 'job_simp_other' else 0

    is_seniorty_0 = 1 if request.form['career level'] == 'seniority_junior' else 0
    is_seniorty_1 = 1 if request.form['career level'] == 'seniority_senior' else 0
    is_seniorty_2 = 1 if request.form['career level'] == 'seniority_na' else 0

    is_pro_0 = 1 if request.form['programming language'] == 'Python' else 0
    is_pro_1 = 1 if request.form['programming language'] == 'R' else 0



    is_state_0 = 1 if request.form['state'] == 'job_location_state_ NM' else 0
    is_state_1 = 1 if request.form['state'] == 'job_location_state_ MD' else 0
    is_state_2 = 1 if request.form['state'] == 'job_location_state_ FL' else 0
    is_state_3 = 1 if request.form['state'] == 'job_location_state_ WA' else 0
    is_state_4 = 1 if request.form['state'] == 'job_location_state_ NY' else 0
    is_state_5 = 1 if request.form['state'] == 'job_location_state_ TX' else 0
    is_state_6 = 1 if request.form['state'] == 'job_location_state_ CA' else 0
    is_state_7 = 1 if request.form['state'] == 'job_location_state_ VA' else 0
    is_state_8 = 1 if request.form['state'] == 'job_location_state_ MA' else 0
    is_state_9 = 1 if request.form['state'] == 'job_location_state_ NJ' else 0
    is_state_10= 1 if request.form['state'] == 'job_location_state_ CO' else 0
    is_state_11= 1 if request.form['state'] == 'job_location_state_ IL' else 0
    is_state_12= 1 if request.form['state'] == 'job_location_state_ KY' else 0
    is_state_13= 1 if request.form['state'] == 'job_location_state_ OR' else 0
    is_state_14= 1 if request.form['state'] == 'job_location_state_ CT' else 0
    is_state_15= 1 if request.form['state'] == 'job_location_state_ MI' else 0
    is_state_16= 1 if request.form['state'] == 'job_location_state_ OH' else 0
    is_state_17= 1 if request.form['state'] == 'job_location_state_ AL' else 0
    is_state_18= 1 if request.form['state'] == 'job_location_state_ MO' else 0
    is_state_19= 1 if request.form['state'] == 'job_location_state_ PA' else 0
    is_state_20= 1 if request.form['state'] == 'job_location_state_ GA' else 0
    is_state_21= 1 if request.form['state'] == 'job_location_state_ IN' else 0
    is_state_22= 1 if request.form['state'] == 'job_location_state_ LA' else 0
    is_state_23= 1 if request.form['state'] == 'job_location_state_ WI' else 0
    is_state_24= 1 if request.form['state'] == 'job_location_state_ NC' else 0
    is_state_25= 1 if request.form['state'] == 'job_location_state_ AZ' else 0
    is_state_26= 1 if request.form['state'] == 'job_location_state_ NE' else 0
    is_state_27= 1 if request.form['state'] == 'job_location_state_ MN' else 0
    is_state_28= 1 if request.form['state'] == 'job_location_state_ DC' else 0
    is_state_29= 1 if request.form['state'] == 'job_location_state_ UT' else 0
    is_state_30= 1 if request.form['state'] == 'job_location_state_ TN' else 0
    is_state_31= 1 if request.form['state'] == 'job_location_state_ DE' else 0
    is_state_32= 1 if request.form['state'] == 'job_location_state_ ID' else 0
    is_state_33= 1 if request.form['state'] == 'job_location_state_ RI' else 0
    is_state_34= 1 if request.form['state'] == 'job_location_state_ IA' else 0
    is_state_35= 1 if request.form['state'] == 'job_location_state_ SC' else 0
    is_state_36= 1 if request.form['state'] == 'job_location_state_ KS' else 0



    is_size_0 = 1 if request.form['size of company'] == 'Size_1 to 50 employees' else 0
    is_size_1 = 1 if request.form['size of company'] == 'Size_51 to 200 employees' else 0
    is_size_2 = 1 if request.form['size of company'] == 'Size_201 to 500 employees' else 0
    is_size_3 = 1 if request.form['size of company'] == 'Size_501 to 1000 employees' else 0
    is_size_4 = 1 if request.form['size of company'] == 'Size_1001 to 5000 employees' else 0
    is_size_5 = 1 if request.form['size of company'] == 'Size_5001 to 10000 employees' else 0
    is_size_6 = 1 if request.form['size of company'] == 'Size_10000+ employees' else 0
    



    is_sector_0 = 1 if request.form['sector'] == 'Sector_Aerospace & Defense' else 0
    is_sector_1 = 1 if request.form['sector'] == 'Sector_Health Care' else 0
    is_sector_2 = 1 if request.form['sector'] == 'Sector_Business Services' else 0
    is_sector_3 = 1 if request.form['sector'] == 'Sector_Oil, Gas, Energy & Utilities' else 0
    is_sector_4 = 1 if request.form['sector'] == 'Sector_Real Estate' else 0
    is_sector_5 = 1 if request.form['sector'] == 'Sector_Finance' else 0
    is_sector_6 = 1 if request.form['sector'] == 'Sector_Information Technology' else 0
    is_sector_7 = 1 if request.form['sector'] == 'Sector_Retail' else 0
    is_sector_8 = 1 if request.form['sector'] == 'Sector_Biotech & Pharmaceuticals' else 0
    is_sector_9 = 1 if request.form['sector'] == 'Sector_Media' else 0
    is_sector_10= 1 if request.form['sector'] == 'Sector_Transportation & Logistics' else 0
    is_sector_11= 1 if request.form['sector'] == 'Sector_Manufacturing' else 0
    is_sector_12= 1 if request.form['sector'] == 'Sector_Mining & Metals' else 0
    is_sector_13= 1 if request.form['sector'] == 'Sector_Government' else 0
    is_sector_14= 1 if request.form['sector'] == 'Sector_Agriculture & Forestry' else 0
    is_sector_15= 1 if request.form['sector'] == 'Sector_Education' else 0
    is_sector_16= 1 if request.form['sector'] == 'Sector_Travel & Tourism' else 0
    is_sector_17= 1 if request.form['sector'] == 'Sector_Non-Profit' else 0
    is_sector_18= 1 if request.form['sector'] == 'Sector_Arts, Entertainment & Recreation' else 0
    is_sector_19= 1 if request.form['sector'] == 'Sector_Construction, Repair & Maintenance' else 0
    is_sector_20= 1 if request.form['sector'] == 'Sector_Accounting & Legal' else 0
    is_sector_21= 1 if request.form['sector'] == 'Sector_Consumer Services' else 0
    is_sector_22 = 1 if request.form['sector'] == 'Sector_Insurance' else 0
    is_sector_23 = 1 if request.form['sector'] == 'Telecommunications' else 0




    
    result = round(model.predict([[is_title_0,is_title_1,is_title_2,is_title_3,is_title_4,is_title_5,is_title_6,
    	is_seniorty_0,is_seniorty_1,is_seniorty_2,is_pro_0,is_pro_1,is_state_0,is_state_1,is_state_2,is_state_3,
    	is_state_4,is_state_5,is_state_6,is_state_7,is_state_8,is_state_9,is_state_10,is_state_11,is_state_12,
    	is_state_13,is_state_14,is_state_15,is_state_16,is_state_17,is_state_18,is_state_19,is_state_20,
    	is_state_21,is_state_22,is_state_23,is_state_24,is_state_25,is_state_26,is_state_27,is_state_28,
    	is_state_29,is_state_30,is_state_31,is_state_32,is_state_33,is_state_34,is_state_35,is_state_36,is_size_0,
    	is_size_1,is_size_2,is_size_3,is_size_4,is_size_5,is_size_6,is_sector_0,is_sector_1,
    	is_sector_2,is_sector_3,is_sector_4,is_sector_5,is_sector_6,is_sector_7,is_sector_8,is_sector_9,
    	is_sector_10,is_sector_11,is_sector_12,is_sector_13,is_sector_14,is_sector_15,is_sector_16,
    	is_sector_17,is_sector_18,is_sector_19,is_sector_20,is_sector_21,is_sector_22,is_sector_23]])[0]*1000)
    return render_template("index.html", result=result)


    

if __name__ == "__main__":
    app.run()






