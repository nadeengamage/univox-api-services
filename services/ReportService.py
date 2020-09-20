"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Generate report business logic.
"""

from app import db

class ReportService:

    """
        Generage the NVQ Report data.
    """
    def generate_nvq_report(self):

        pref_1 = 'INSERT INTO tbl_temp_nvq ( student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type ) SELECT tbl_students_marks.std_mark_student_id, tbl_students_marks.std_marks, tbl_students.std_student_type, tbl_degrees.deg_degree_code, "1" AS Category, "B1" AS BatchType FROM UnivoxDB.tbl_students_marks INNER JOIN UnivoxDB.tbl_students ON ( tbl_students_marks.std_mark_student_id = tbl_students.id ), UnivoxDB.tbl_degrees INNER JOIN UnivoxDB.tbl_criterias ON (tbl_degrees.id = tbl_criterias.crt_degree_id) WHERE ( tbl_students.std_preference_1 = tbl_degrees.deg_degree_code ) AND tbl_students_marks.std_marks >= tbl_criterias.crt_btch_two_cut_off_mark AND tbl_students_marks.std_mark_student_id NOT IN ( SELECT student_id FROM tbl_temp_nvq ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details WHERE std_batch_type = "B1" )'
        db.engine.execute(pref_1)
        
        
        pref_2 = 'INSERT INTO tbl_temp_nvq ( student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type ) SELECT tbl_students_marks.std_mark_student_id, tbl_students_marks.std_marks, tbl_students.std_student_type, tbl_degrees.deg_degree_code, "2" AS Category, "B1" AS BatchType FROM UnivoxDB.tbl_students_marks INNER JOIN UnivoxDB.tbl_students ON ( tbl_students_marks.std_mark_student_id = tbl_students.id ), UnivoxDB.tbl_degrees INNER JOIN UnivoxDB.tbl_criterias ON (tbl_degrees.id = tbl_criterias.crt_degree_id) WHERE ( tbl_students.std_preference_2 = tbl_degrees.deg_degree_code ) AND tbl_students_marks.std_marks >= tbl_criterias.crt_btch_two_cut_off_mark AND tbl_students_marks.std_mark_student_id NOT IN ( SELECT student_id FROM tbl_temp_nvq ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details WHERE std_batch_type = "B1" )'
        db.engine.execute(pref_2)
        

        pref_3 = 'INSERT INTO tbl_temp_nvq ( student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type ) SELECT tbl_students_marks.std_mark_student_id, tbl_students_marks.std_marks, tbl_students.std_student_type, tbl_degrees.deg_degree_code, "3" AS Category, "B1" AS BatchType FROM UnivoxDB.tbl_students_marks INNER JOIN UnivoxDB.tbl_students ON ( tbl_students_marks.std_mark_student_id = tbl_students.id ), UnivoxDB.tbl_degrees INNER JOIN UnivoxDB.tbl_criterias ON (tbl_degrees.id = tbl_criterias.crt_degree_id) WHERE ( tbl_students.std_preference_3 = tbl_degrees.deg_degree_code ) AND tbl_students_marks.std_marks >= tbl_criterias.crt_btch_two_cut_off_mark AND tbl_students_marks.std_mark_student_id NOT IN ( SELECT student_id FROM tbl_temp_nvq ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details WHERE std_batch_type = "B1" )'
        db.engine.execute(pref_3)
    
    """
        Generage the AL Report data.
    """
    def generate_al_report(self):
        pref_1 = 'INSERT INTO tbl_temp_al (student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type) SELECT tbl_student_al_details.std_al_student_id , tbl_student_al_details.std_al_z_score , tbl_students.std_student_type , tbl_degrees.deg_degree_code ,"1" AS Category ,"B1" AS BatchType FROM UnivoxDB.tbl_student_al_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_al_details.std_al_student_id = tbl_students.id) , UnivoxDB.tbl_criterias INNER JOIN UnivoxDB.tbl_degrees ON (tbl_criterias.crt_degree_id = tbl_degrees.id) WHERE (tbl_students.std_preference_1 = tbl_degrees.deg_degree_code) AND tbl_student_al_details.std_al_z_score >=tbl_criterias.crt_btch_one_al_cut_off_mark AND tbl_student_al_details.std_al_student_id NOT IN (SELECT student_id FROM tbl_temp_al)'
        db.engine.execute(pref_1)

        
        pref_2 = 'INSERT INTO tbl_temp_al (student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type) SELECT tbl_student_al_details.std_al_student_id , tbl_student_al_details.std_al_z_score , tbl_students.std_student_type , tbl_degrees.deg_degree_code ,"2" AS Category ,"B1" AS BatchType FROM UnivoxDB.tbl_student_al_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_al_details.std_al_student_id = tbl_students.id) , UnivoxDB.tbl_criterias INNER JOIN UnivoxDB.tbl_degrees ON (tbl_criterias.crt_degree_id = tbl_degrees.id) WHERE (tbl_students.std_preference_2 = tbl_degrees.deg_degree_code) AND tbl_student_al_details.std_al_z_score >=tbl_criterias.crt_btch_one_al_cut_off_mark AND tbl_student_al_details.std_al_student_id NOT IN (SELECT student_id FROM tbl_temp_al)'
        db.engine.execute(pref_2)

        
        pref_3 = 'INSERT INTO tbl_temp_al (student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type) SELECT tbl_student_al_details.std_al_student_id , tbl_student_al_details.std_al_z_score , tbl_students.std_student_type , tbl_degrees.deg_degree_code ,"3" AS Category ,"B1" AS BatchType FROM UnivoxDB.tbl_student_al_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_al_details.std_al_student_id = tbl_students.id) , UnivoxDB.tbl_criterias INNER JOIN UnivoxDB.tbl_degrees ON (tbl_criterias.crt_degree_id = tbl_degrees.id) WHERE (tbl_students.std_preference_3 = tbl_degrees.deg_degree_code) AND tbl_student_al_details.std_al_z_score >=tbl_criterias.crt_btch_one_al_cut_off_mark AND tbl_student_al_details.std_al_student_id NOT IN (SELECT student_id FROM tbl_temp_al)'
        db.engine.execute(pref_3)
