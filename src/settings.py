import os
from typing import Iterable, List

# Original Files
fn_data = 'data/rli-psn'
psn_ent_anon = f'{fn_data}/peoplesun_ent_anon.csv'
psn_entapps_anon = f'{fn_data}/peoplesun_entapps_anon.csv'
psn_entequips_anon = f'{fn_data}/peoplesun_entequips_anon.csv'
psn_entstoves_anon = f'{fn_data}/peoplesun_entstoves_anon.csv'
psn_hh_anon = f'{fn_data}/peoplesun_hh_anon.csv'
psn_hhapps_anon = f'{fn_data}/peoplesun_hhapps_anon.csv'
psn_hhstoves_anon = f'{fn_data}/peoplesun_hhstoves_anon.csv'
psn_enumarea_anon = f'{fn_data}/eaidgeokey_anon.csv'

psn_ent_odk_choices = f'{fn_data}/peoplesun_ent_odk_choices.xlsx'
psn_ent_odk_codebook = f'{fn_data}/peoplesun_ent_odk_codebook.xlsx'
psn_hh_odk_choices = f'{fn_data}/peoplesun_hh_odk_choices.xlsx'
psn_hh_odk_codebook = f'{fn_data}/peoplesun_hh_odk_codebook.xlsx'

psn_ent_odk_choices_csv = f'{fn_data}/peoplesun_ent_odk_choices_Sheet1.csv'
psn_ent_odk_codebook_csv = f'{fn_data}/peoplesun_ent_odk_codebook_Sheet1.csv'
psn_hh_odk_choices_csv = f'{fn_data}/peoplesun_hh_odk_choices_Sheet1.csv'
psn_hh_odk_codebook_csv = f'{fn_data}/peoplesun_hh_odk_codebook_Sheet1.csv'

# Output Files
psn_ent_anon_new = f'{fn_data}/result/peoplesun_enterprise_energy_audit.csv'
psn_hh_anon_new = f'{fn_data}/result/peoplesun_household_energy_audit.csv'
psn_entapps_anon_new = f'{fn_data}/result/peoplesun_enterprise_key_appliances.csv'
psn_entequips_anon_new = f'{fn_data}/result/peoplesun_enterprise_key_equipments.csv'
psn_entstoves_anon_new = f'{fn_data}/result/peoplesun_enterprise_key_stoves.csv'
psn_hhapps_anon_new = f'{fn_data}/result/peoplesun_household_key_appliances.csv'
psn_hhstoves_anon_new = f'{fn_data}/result/peoplesun_household_key_stoves.csv'

psn_ent_odk_choices_csv_new = f'{fn_data}/result/peoplesun_enterprise_key_odk_choices.csv'
psn_ent_odk_codebook_csv_new = f'{fn_data}/result/peoplesun_enterprise_key_odk_codebook.csv'
psn_hh_odk_choices_csv_new = f'{fn_data}/result/peoplesun_household_key_odk_choices.csv'
psn_hh_odk_codebook_csv_new = f'{fn_data}/result/peoplesun_household_key_odk_codebook.csv'

ent_region = f'{fn_data}/result/peoplesun_enterprise_key_regions.csv'
hh_region = f'{fn_data}/result/peoplesun_household_key_regions.csv'

psn_enumarea_anon_new = f'{fn_data}/result/peoplesun_key_enumeration_area.csv'

psn_ent_long = f'{fn_data}/result/peoplesun_enterprise_energy_audit_normalised.csv'
psn_hh_long = f'{fn_data}/result/peoplesun_household_energy_audit_normalised.csv'

filepath_list = [
    psn_ent_anon_new,
    psn_hh_anon_new,
    psn_entapps_anon_new,
    psn_entequips_anon_new,
    psn_entstoves_anon_new,
    psn_hhapps_anon_new,
    psn_hhstoves_anon_new,

    psn_ent_odk_choices_csv_new,
    psn_ent_odk_codebook_csv_new,
    psn_hh_odk_choices_csv_new,
    psn_hh_odk_codebook_csv_new,

    ent_region,
    hh_region,
    psn_enumarea_anon_new,

    psn_ent_long,
    psn_hh_long
]

def extract_filenames(filepath_list: Iterable[str]) -> List[str]:
    """
    Extract filenames without file extensions from a list of file paths.

    Parameters
    ----------
    filepath_list : Iterable[str]
        List or iterable of file paths.

    Returns
    -------
    List[str]
        List of filenames without extensions.
    """
    return [
        os.path.splitext(os.path.basename(filepath))[0]
        for filepath in filepath_list
    ]
