
from app import db

class ReportService:

    def generate_nvq_report(self):

        pref_1 = 'INSERT INTO tbl_temp_nvq ( student_id, student_marks, std_student_type, deg_degree_code, preferance_type, student_type ) SELECT tbl_students_marks.std_mark_student_id, tbl_students_marks.std_marks, tbl_students.std_student_type, tbl_degrees.deg_degree_code, "PRE1" AS Category, "B2" AS BatchType FROM UnivoxDB.tbl_students_marks INNER JOIN UnivoxDB.tbl_students ON ( tbl_students_marks.std_mark_student_id = tbl_students.id ), UnivoxDB.tbl_degrees INNER JOIN UnivoxDB.tbl_criterias ON (tbl_degrees.id = tbl_criterias.crt_degree_id) WHERE ( tbl_students.std_preference_1 = tbl_degrees.deg_degree_code ) AND tbl_students_marks.std_marks >= tbl_criterias.crt_btch_two_cut_off_mark AND tbl_students_marks.std_mark_student_id NOT IN ( SELECT student_id FROM tbl_temp_nvq ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details WHERE std_batch_type = "B2" )'
        res_1 = db.engine.execute(pref_1)
        
        
        pref_2 = 'INSERT INTO tbl_temp_nvq ( student_id, student_marks, std_student_type, deg_degree_code, preferance_type, student_type ) SELECT tbl_students_marks.std_mark_student_id, tbl_students_marks.std_marks, tbl_students.std_student_type, tbl_degrees.deg_degree_code, "PRE2" AS Category, "B2" AS BatchType FROM UnivoxDB.tbl_students_marks INNER JOIN UnivoxDB.tbl_students ON ( tbl_students_marks.std_mark_student_id = tbl_students.id ), UnivoxDB.tbl_degrees INNER JOIN UnivoxDB.tbl_criterias ON (tbl_degrees.id = tbl_criterias.crt_degree_id) WHERE ( tbl_students.std_preference_2 = tbl_degrees.deg_degree_code ) AND tbl_students_marks.std_marks >= tbl_criterias.crt_btch_two_cut_off_mark AND tbl_students_marks.std_mark_student_id NOT IN ( SELECT student_id FROM tbl_temp_nvq ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details WHERE std_batch_type = "B2" )'
        res_2 = db.engine.execute(pref_2)
        

        pref_3 = 'SELECT tbl_students_marks.std_mark_student_id, tbl_students_marks.std_marks, tbl_students.std_student_type, tbl_degrees.deg_degree_code, "PRE3" AS Category, "B2" AS BatchType FROM UnivoxDB.tbl_students_marks INNER JOIN UnivoxDB.tbl_students ON ( tbl_students_marks.std_mark_student_id = tbl_students.id ), UnivoxDB.tbl_degrees INNER JOIN UnivoxDB.tbl_criterias ON (tbl_degrees.id = tbl_criterias.crt_degree_id) WHERE ( tbl_students.std_preference_3 = tbl_degrees.deg_degree_code ) AND tbl_students_marks.std_marks >= tbl_criterias.crt_btch_two_cut_off_mark AND tbl_students_marks.std_mark_student_id NOT IN ( SELECT student_id FROM tbl_temp_nvq ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details ) AND tbl_students_marks.std_mark_student_id IN ( SELECT id FROM tbl_student_nvq_details WHERE std_batch_type = "B2" )'
        res_3 = db.engine.execute(pref_3)
        