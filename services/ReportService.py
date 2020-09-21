"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Generate report business logic.
"""

from app import db
from sqlalchemy.sql import text

class ReportService:

    """
        Generage the NVQ Report data.
    """
    def generate_nvq_report(self, batch_type, identity):

        data = { 'batch_type': batch_type, 'identity': identity}

        # Delete all existing data in the table
        delete_sql = 'DELETE FROM tbl_temp_nvq'
        db.engine.execute(delete_sql)


        pref_1 = text('INSERT INTO tbl_temp_nvq ( student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type, created_by ) SELECT tbl_students_marks.std_mark_student_id, tbl_students_marks.std_marks, tbl_students.std_student_type, tbl_degrees.deg_degree_code, "1" AS Category, :batch_type AS BatchType, :identity AS created_by  FROM UnivoxDB.tbl_students_marks INNER JOIN UnivoxDB.tbl_students ON ( tbl_students_marks.std_mark_student_id = tbl_students.id ), UnivoxDB.tbl_degrees INNER JOIN UnivoxDB.tbl_criterias ON (tbl_degrees.id = tbl_criterias.crt_degree_id) WHERE ( tbl_students.std_preference_1 = tbl_degrees.deg_degree_code ) AND tbl_students_marks.std_marks >= tbl_criterias.crt_btch_two_cut_off_mark AND tbl_students_marks.std_mark_student_id NOT IN ( SELECT student_id FROM tbl_temp_nvq ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details WHERE std_batch_type = :batch_type  )')
        db.engine.execute(pref_1, data)
        
        
        pref_2 = text('INSERT INTO tbl_temp_nvq ( student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type, created_by ) SELECT tbl_students_marks.std_mark_student_id, tbl_students_marks.std_marks, tbl_students.std_student_type, tbl_degrees.deg_degree_code, "2" AS Category, :batch_type AS BatchType, :identity AS created_by FROM UnivoxDB.tbl_students_marks INNER JOIN UnivoxDB.tbl_students ON ( tbl_students_marks.std_mark_student_id = tbl_students.id ), UnivoxDB.tbl_degrees INNER JOIN UnivoxDB.tbl_criterias ON (tbl_degrees.id = tbl_criterias.crt_degree_id) WHERE ( tbl_students.std_preference_2 = tbl_degrees.deg_degree_code ) AND tbl_students_marks.std_marks >= tbl_criterias.crt_btch_two_cut_off_mark AND tbl_students_marks.std_mark_student_id NOT IN ( SELECT student_id FROM tbl_temp_nvq ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details WHERE std_batch_type = :batch_type  )')
        db.engine.execute(pref_2, data)
        

        pref_3 = text('INSERT INTO tbl_temp_nvq ( student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type, created_by ) SELECT tbl_students_marks.std_mark_student_id, tbl_students_marks.std_marks, tbl_students.std_student_type, tbl_degrees.deg_degree_code, "3" AS Category, :batch_type AS BatchType, :identity AS created_by FROM UnivoxDB.tbl_students_marks INNER JOIN UnivoxDB.tbl_students ON ( tbl_students_marks.std_mark_student_id = tbl_students.id ), UnivoxDB.tbl_degrees INNER JOIN UnivoxDB.tbl_criterias ON (tbl_degrees.id = tbl_criterias.crt_degree_id) WHERE ( tbl_students.std_preference_3 = tbl_degrees.deg_degree_code ) AND tbl_students_marks.std_marks >= tbl_criterias.crt_btch_two_cut_off_mark AND tbl_students_marks.std_mark_student_id NOT IN ( SELECT student_id FROM tbl_temp_nvq ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details WHERE std_batch_type = :batch_type  )')
        db.engine.execute(pref_3, data)
        
    
    """
        Generage the AL Report data.
    """
    def generate_al_report(self, identity):

        data = {'identity': identity}

        # Delete all records
        delete_sql = 'DELETE FROM tbl_temp_al'
        db.engine.execute(delete_sql)


        pref_1 = text('INSERT INTO tbl_temp_al ( student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type, created_by ) SELECT tbl_student_al_details.std_al_student_id , tbl_student_al_details.std_al_z_score , tbl_students.std_student_type , tbl_degrees.deg_degree_code ,"1" AS Category ,"B1" AS BatchType, :identity as created_by FROM UnivoxDB.tbl_student_al_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_al_details.std_al_student_id = tbl_students.id) , UnivoxDB.tbl_criterias INNER JOIN UnivoxDB.tbl_degrees ON (tbl_criterias.crt_degree_id = tbl_degrees.id) WHERE (tbl_students.std_preference_1 = tbl_degrees.deg_degree_code) AND tbl_student_al_details.std_al_z_score >=tbl_criterias.crt_btch_one_al_cut_off_mark AND tbl_student_al_details.std_al_student_id NOT IN (SELECT student_id FROM tbl_temp_al)')
        db.engine.execute(pref_1, data)

        
        pref_2 = text('INSERT INTO tbl_temp_al ( student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type, created_by ) SELECT tbl_student_al_details.std_al_student_id , tbl_student_al_details.std_al_z_score , tbl_students.std_student_type , tbl_degrees.deg_degree_code ,"2" AS Category ,"B1" AS BatchType, :identity as created_by FROM UnivoxDB.tbl_student_al_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_al_details.std_al_student_id = tbl_students.id) , UnivoxDB.tbl_criterias INNER JOIN UnivoxDB.tbl_degrees ON (tbl_criterias.crt_degree_id = tbl_degrees.id) WHERE (tbl_students.std_preference_2 = tbl_degrees.deg_degree_code) AND tbl_student_al_details.std_al_z_score >=tbl_criterias.crt_btch_one_al_cut_off_mark AND tbl_student_al_details.std_al_student_id NOT IN (SELECT student_id FROM tbl_temp_al)')
        db.engine.execute(pref_2, data)

        
        pref_3 = text('INSERT INTO tbl_temp_al ( student_id, student_marks, std_student_type, deg_degree_code, preferance_type, batch_type, created_by ) SELECT tbl_student_al_details.std_al_student_id , tbl_student_al_details.std_al_z_score , tbl_students.std_student_type , tbl_degrees.deg_degree_code ,"3" AS Category ,"B1" AS BatchType, :identity as created_by FROM UnivoxDB.tbl_student_al_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_al_details.std_al_student_id = tbl_students.id) , UnivoxDB.tbl_criterias INNER JOIN UnivoxDB.tbl_degrees ON (tbl_criterias.crt_degree_id = tbl_degrees.id) WHERE (tbl_students.std_preference_3 = tbl_degrees.deg_degree_code) AND tbl_student_al_details.std_al_z_score >=tbl_criterias.crt_btch_one_al_cut_off_mark AND tbl_student_al_details.std_al_student_id NOT IN (SELECT student_id FROM tbl_temp_al)')
        db.engine.execute(pref_3, data)


    def get_nvq_applicants_count_by_degree_code(self, applicants_count, degree, batch_type):
        data = {'degree_code': degree, 'batch_type': batch_type, 'applicants_count': applicants_count}
        sql = text("SELECT count(*) as count FROM UnivoxDB.tbl_student_nvq_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_nvq_details.std_nvq_student_id = tbl_students.id) INNER JOIN UnivoxDB.tbl_temp_nvq ON (tbl_temp_nvq.student_id = tbl_student_nvq_details.std_nvq_student_id) WHERE batch_type = :batch_type AND deg_degree_code = :degree_code ORDER BY student_marks DESC, preferance_type ASC LIMIT :applicants_count")
        return db.engine.execute(sql, data)


    def get_nvq_applicants_by_degree_code(self, applicants_count, degree, batch_type):
        data = {'degree_code': degree, 'batch_type': batch_type, 'applicants_count': applicants_count}
        sql = text("SELECT tbl_student_nvq_details.std_application_no , tbl_temp_nvq.deg_degree_code , tbl_students.std_student_type ,tbl_students.std_initials ,tbl_students.std_surename ,tbl_students.std_title ,tbl_students.std_gender ,tbl_students.std_address_1 ,tbl_students.std_address_2 ,tbl_students.std_address_3 ,tbl_students.std_district ,tbl_temp_nvq.student_marks ,tbl_students.std_telephone ,tbl_temp_nvq.preferance_type FROM UnivoxDB.tbl_student_nvq_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_nvq_details.std_nvq_student_id = tbl_students.id) INNER JOIN UnivoxDB.tbl_temp_nvq ON (tbl_temp_nvq.student_id = tbl_student_nvq_details.std_nvq_student_id) WHERE batch_type = :batch_type AND deg_degree_code = :degree_code ORDER BY student_marks DESC, preferance_type ASC LIMIT :applicants_count")
        return db.engine.execute(sql, data)

    
    def get_al_applicants_by_degree_code(self, applicants_count, degree, batch_type):
        data = {'degree_code': degree, 'applicants_count': applicants_count}
        sql = text("SELECT tbl_student_al_details.std_application_no , tbl_temp_al.deg_degree_code , tbl_students.std_student_type ,tbl_students.std_initials ,tbl_students.std_surename ,tbl_students.std_title ,tbl_students.std_gender ,tbl_students.std_address_1 ,tbl_students.std_address_2 ,tbl_students.std_address_3 ,tbl_students.std_district , tbl_temp_al.student_marks ,tbl_students.std_telephone ,tbl_temp_al.preferance_type FROM UnivoxDB.tbl_student_al_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_al_details.std_al_student_id = tbl_students.id) INNER JOIN UnivoxDB.tbl_temp_al ON (tbl_temp_al.student_id = tbl_student_al_details.std_al_student_id) WHERE deg_degree_code = :degree_code ORDER BY student_marks DESC, preferance_type ASC LIMIT :applicants_count")
        return db.engine.execute(sql, data)

    def get_nvq_al_applicants_by_degree_code(self, nvq_applicants_count, al_applicants_count, degree, batch_type):
        data = {'nvq_applicants_count': nvq_applicants_count, 'al_applicants_count': al_applicants_count, 'degree_code': degree}
        sql = text("SELECT * FROM (( SELECT tbl_student_al_details.std_application_no , tbl_temp_al.deg_degree_code , tbl_students.std_student_type ,tbl_students.std_initials ,tbl_students.std_surename ,tbl_students.std_title ,tbl_students.std_gender ,tbl_students.std_address_1 ,tbl_students.std_address_2 ,tbl_students.std_address_3 ,tbl_students.std_district , tbl_temp_al.student_marks ,tbl_students.std_telephone ,tbl_temp_al.preferance_type FROM UnivoxDB.tbl_student_al_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_al_details.std_al_student_id = tbl_students.id) INNER JOIN UnivoxDB.tbl_temp_al ON (tbl_temp_al.student_id = tbl_student_al_details.std_al_student_id) WHERE deg_degree_code = :degree_code LIMIT :al_applicants_count UNION SELECT tbl_student_nvq_details.std_application_no , tbl_temp_nvq.deg_degree_code , tbl_students.std_student_type ,tbl_students.std_initials ,tbl_students.std_surename ,tbl_students.std_title ,tbl_students.std_gender ,tbl_students.std_address_1 ,tbl_students.std_address_2 ,tbl_students.std_address_3 ,tbl_students.std_district ,tbl_temp_nvq.student_marks ,tbl_students.std_telephone ,tbl_temp_nvq.preferance_type FROM UnivoxDB.tbl_student_nvq_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_nvq_details.std_nvq_student_id = tbl_students.id) INNER JOIN UnivoxDB.tbl_temp_nvq ON (tbl_temp_nvq.student_id = tbl_student_nvq_details.std_nvq_student_id) WHERE batch_type = 'B1' AND deg_degree_code = :degree_code LIMIT :nvq_applicants_count ) ORDER BY deg_degree_code ASC , std_student_type DESC ,preferance_type ASC ,student_marks DESC ) AS T")
        return db.engine.execute(sql, data)

    def get_applicants_b2_with_degree_code(self, applicant_count, degree):
        data = {'degree_code': degree, 'applicant_count': applicant_count}
        sql = text("SELECT tbl_student_nvq_details.std_application_no , tbl_temp_nvq.deg_degree_code , tbl_students.std_student_type ,tbl_students.std_initials ,tbl_students.std_surename ,tbl_students.std_title ,tbl_students.std_gender ,tbl_students.std_address_1 ,tbl_students.std_address_2 ,tbl_students.std_address_3 ,tbl_students.std_district ,tbl_temp_nvq.student_marks ,tbl_students.std_telephone FROM UnivoxDB.tbl_student_nvq_details INNER JOIN UnivoxDB.tbl_students ON (tbl_student_nvq_details.std_nvq_student_id = tbl_students.id) INNER JOIN UnivoxDB.tbl_temp_nvq ON (tbl_temp_nvq.student_id = tbl_student_nvq_details.std_nvq_student_id) WHERE batch_type = 'B2' AND deg_degree_code = :degree_code ORDER BY deg_degree_code ASC,preferance_type ASC ,student_marks DESC LIMIT :applicant_count")
        return db.engine.execute(sql, data)