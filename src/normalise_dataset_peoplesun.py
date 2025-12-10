
import os
from shutil import copy
from split_xlsx_to_csvs import split_xlsx_to_csvs
import pandas as pd


def copy_csv_pandas(csv_path, output_path, sep=";"):
    df = pd.read_csv(csv_path, low_memory = False)
    df = df.replace(';', '.')
    df.to_csv(output_path, encoding = 'utf-8', sep = ';', index = False)

    return output_path


if __name__ == '__main__':

    import json
    from getpass import getpass
    from os import environ
    import requests as req

    # Files
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

    # Excel Split
    csv_files = split_xlsx_to_csvs(psn_ent_odk_choices, output_dir = f"{fn_data}")
    csv_files = split_xlsx_to_csvs(psn_ent_odk_codebook, output_dir = f"{fn_data}")
    csv_files = split_xlsx_to_csvs(psn_hh_odk_choices, output_dir = f"{fn_data}")
    csv_files = split_xlsx_to_csvs(psn_hh_odk_codebook, output_dir = f"{fn_data}")
    print("Create CSV files from Excel")

    # Copy and Rename
    psn_ent_anon_new = f'{fn_data}/result/peoplesun_enterprise_energy_audit.csv'
    copy(psn_ent_anon, psn_ent_anon_new)
    print("Copy and Rename:", psn_ent_anon_new)

    psn_hh_anon_new = f'{fn_data}/result/peoplesun_household_energy_audit.csv'
    copy(psn_hh_anon, psn_hh_anon_new)
    print("Copy and Rename:", psn_hh_anon_new)

    # Additional Data
    psn_entapps_anon_new = f'{fn_data}/result/peoplesun_enterprise_key_appliances.csv'
    copy_csv_pandas(psn_entapps_anon, psn_entapps_anon_new)

    psn_entequips_anon_new = f'{fn_data}/result/peoplesun_enterprise_key_equipments.csv'
    copy_csv_pandas(psn_entequips_anon, psn_entequips_anon_new)

    psn_entstoves_anon_new = f'{fn_data}/result/peoplesun_enterprise_key_stoves.csv'
    copy_csv_pandas(psn_entstoves_anon, psn_entstoves_anon_new)

    psn_hhapps_anon_new = f'{fn_data}/result/peoplesun_household_key_appliances.csv'
    copy_csv_pandas(psn_hhapps_anon, psn_hhapps_anon_new)

    psn_hhstoves_anon_new = f'{fn_data}/result/peoplesun_household_key_stoves.csv'
    copy_csv_pandas(psn_hhstoves_anon, psn_hhstoves_anon_new)
    print("Copy and Rename: Additional Data")

    # Keys and Codes
    psn_ent_odk_choices_csv = f'{fn_data}/peoplesun_ent_odk_choices_Sheet1.csv'
    psn_ent_odk_codebook_csv = f'{fn_data}/peoplesun_ent_odk_codebook_Sheet1.csv'
    psn_hh_odk_choices_csv = f'{fn_data}/peoplesun_hh_odk_choices_Sheet1.csv'
    psn_hh_odk_codebook_csv = f'{fn_data}/peoplesun_hh_odk_codebook_Sheet1.csv'

    psn_ent_odk_choices_csv_new = f'{fn_data}/result/peoplesun_enterprise_key_odk_choices.csv'
    psn_ent_odk_codebook_csv_new = f'{fn_data}/result/peoplesun_enterprise_key_odk_codebook.csv'
    psn_hh_odk_choices_csv_new = f'{fn_data}/result/peoplesun_household_key_odk_choices.csv'
    psn_hh_odk_codebook_csv_new = f'{fn_data}/result/peoplesun_household_key_odk_codebook.csv'

    copy(psn_ent_odk_choices_csv, psn_ent_odk_choices_csv_new)
    copy(psn_ent_odk_codebook_csv, psn_ent_odk_codebook_csv_new)
    copy(psn_hh_odk_choices_csv, psn_hh_odk_choices_csv_new)
    copy(psn_hh_odk_codebook_csv, psn_hh_odk_codebook_csv_new)
    print("Copy and Rename: Keys and Codes")

    # Delete CSV
    os.remove(psn_ent_odk_choices_csv)
    os.remove(psn_ent_odk_codebook_csv)
    os.remove(psn_hh_odk_choices_csv)
    os.remove(psn_hh_odk_codebook_csv)
    print("Delete CSV")

    # Geodata
    psn_enumarea_anon_new = f'{fn_data}/result/peoplesun_key_enumeration_area.csv'
    copy_csv_pandas(psn_enumarea_anon, psn_enumarea_anon_new)
    print("Copy and Rename: Enumeration Area")

    # Normalise Data

    # Enterprise
    df_enterprise = pd.read_csv(psn_ent_anon_new, low_memory=False)
    # print(df_enterprise.columns)

    df_ent_region = df_enterprise[['entid','zone','state','eaid','lga','urca_cat']].copy()
    ent_region = f'{fn_data}/result/peoplesun_enterprise_key_regions.csv'
    df_ent_region.to_csv(ent_region, encoding = 'utf-8', index = False)
    print(f'Extract region data as:" {ent_region}')

    df_enterprise_norm = df_enterprise.drop(['zone','state','eaid','lga','urca_cat'], axis=1)
    df_enterprise_norm = df_enterprise_norm.replace(';', '.')
    column_list = df_enterprise_norm.columns.drop('entid')
    # print(column_list)
    df_enterprise_norm_long = pd.melt(df_enterprise_norm,
                                      id_vars=['entid'], var_name='question',
                                      value_name='value')

    psn_ent_long = f'{fn_data}/result/peoplesun_enterprise_energy_audit_normalised.csv'
    df_enterprise_norm_long.to_csv(psn_ent_long, encoding = 'utf-8', sep = ';', index = False)
    print(f'Export normalised enterprise data as:" {psn_ent_long}')


    # Households
    df_household = pd.read_csv(psn_hh_anon_new, low_memory = False)
    # print(df_household.columns)

    df_hh_region = df_household[
        ['hhid', 'zone', 'state', 'eaid', 'lga', 'urca_cat']].copy()
    hh_region = f'{fn_data}/result/peoplesun_household_key_regions.csv'
    df_ent_region.to_csv(hh_region, encoding = 'utf-8', index = False)
    print(f'Extract region data as:" {hh_region}')

    df_household_norm = df_household.drop(
        ['zone', 'state', 'eaid', 'lga', 'urca_cat'], axis = 1)
    df_household_norm = df_household_norm.replace(';', '.')
    column_list = df_household_norm.columns.drop('hhid')
    # print(column_list)
    df_household_norm_long = pd.melt(df_household_norm,
                                      id_vars = ['hhid'], var_name = 'question',
                                      value_name = 'value')

    psn_ent_long = f'{fn_data}/result/peoplesun_enterprise_energy_audit_normalised.csv'
    df_household_norm_long.to_csv(psn_ent_long, encoding = 'utf-8', sep = ';',
                                   index = False)

    psn_hh_long = f'{fn_data}/result/peoplesun_household_energy_audit_normalised.csv'
    df_household_norm_long.to_csv(psn_hh_long, encoding = 'utf-8', sep = ';', index = False)
    print(f'Export normalised household data as:" {psn_hh_long}')
