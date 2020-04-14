true = True
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED, NUMERIC, DATETIME, BOOLEAN
from whoosh.analysis import StemmingAnalyzer
import whoosh.reading
import os, os.path
import whoosh.index
from whoosh.qparser import QueryParser
from flask import Flask, render_template, request, redirect, abort, json, send_file,url_for, jsonify
from flask_caching import Cache
from flask_paginate import Pagination, get_page_args, get_page_parameter
from elasticsearch import Elasticsearch
import json
import psycopg2
import sys
import csv
import xlwt
from pandas import DataFrame
import random
import re
import secret
import pysolr 
import sqlalchemy
import socket
import ssl
import time
import requests
from bs4 import BeautifulSoup
import urllib.request
import simplejson
import pprint
import sys
import pandas as pd
# import flask.ext.whooshalchemy

app = Flask(__name__, static_folder='static')

def get_results(list, offset=0, per_page=5):
    return list[offset: offset + per_page]

def findTextBetween(string, start, end):
  start = string.find(start) + len(start)
  end = string.find(end)
  substring = string[start:end]
  return substring

if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    #cache = Cache(app, config={"CACHE_TYPE": "simple"})


    VARIABLE_DESCRIPTION_FILE = "variable_description.json"
    variable_description = {}
    DATASET_LIST_FILE = "dataset_list.json"
    dataset_list = {}


    #@app.route("/static/css/index.css")
    #def css():
    #    print("yolo queue")
    #    response=make_response(render_template("static/css/index.css"))
    #    response.headers["Cache-Control"]="no-cache"
    #    return response


    #csv = "/Users/Billy/Desktop/RossRC2020/finalnot10k.csv"
    #csv = "/Users/Billy/Desktop/RossRC2020/100k8k10q10kscrapped.csv"
    # csv = "/Users/Billy/Desktop/RossRC2020/5000not10ks4testfilesFINAL.csv"
    # df = pd.read_csv(csv)

    # consolidatedIndexID_df = df['consolidated_index_id']
    # companyName_df = df['companyname']
    # formType_df = df['formtype']
    # cik_df = df['cik']
    # dateFiled_df = df['datefiled']
    # url_df = df['filename']
    # content_df = df['Content']

    # consolidatedIndexID_List = consolidatedIndexID_df.tolist()
    # companyName_List = companyName_df.tolist()
    # formType_List = formType_df.tolist()
    # cik_List = cik_df.tolist()
    # dateFiled_List = dateFiled_df.tolist()
    # url_List = url_df.tolist()
    # content_List = content_df.tolist()

    #csv = "/Users/Billy/Desktop/RossRC2020/NewScrape/300Form10K8K2018Scraped.csv"
    csv = "ScrapedCSV/300Form10K8K2018Scraped.csv"
    df = pd.read_csv(csv)

    accession_number_list = df['Accession Number']
    irs_number_list =  df['IRS Number']
    company_name_list = df['Company Name']
    sic_list = df['SIC']
    cik_list = df['CIK']
    industry_list = df['Industry']
    office_list = df['Office']
    state_of_incorporation_list = df['State of Incorporation'] 
    fiscal_year_end_list = df['Fiscal Year End']
    form_type_list = df['Form Type']
    file_number_list = df['Filing Number']
    period_of_report_list = df['Period of Report']
    filing_date_list = df['Filing Date']
    acceptance_date_list = df['Acceptance Date']
    acceptance_time_list = df['Acceptance Time']
    number_of_documents_list = _of_documents_submitted_list = df['Number of Documents Submitted']
    items_list = df['Items']
    business_address_list = df['Business Address'] 
    business_phone_number_list = df['Business Phone Number']
    document_url_list = df['SEC EDGAR URL']
    complete_text_file_url_list = df['Complete Text File URL']
    complete_text_file_size_list = df['Text File Size']
    scraped_document_list = df['Scraped Text File']

    # schema = Schema(ConslidatedIndexId = TEXT(stored=True),
    #                 CompanyName = TEXT(stored=True),
    #                 FormType = TEXT(stored=True),
    #                 CIK = TEXT(stored=True),
    #                 DateFiled = TEXT(stored=True),
    #                 URL = TEXT(stored=True),
    #                 Content = TEXT(stored=True))
    schema = Schema(AccessionNumber = TEXT(stored=True),
                    IRSNumber = TEXT(stored=True),
                    CIK = TEXT(stored=True),
                    CompanyName = TEXT(stored=True),
                    SIC = TEXT(stored=True),
                    Industry = TEXT(stored=True),
                    Office = TEXT(stored=True),
                    StateOfIncorporation = TEXT(stored=True),
                    FiscalYearEnd = TEXT(stored=True),
                    FormType = TEXT(stored=True),
                    FilingNumber = TEXT(stored=True),
                    PeriodOfReport = TEXT(stored=True),
                    FilingDate = TEXT(stored=True),
                    AcceptanceDate = TEXT(stored=True),
                    AcceptanceTime = TEXT(stored=True),
                    NumberOfDocuments = TEXT(stored=True),
                    Items = TEXT(stored=True),
                    BusinessAddress = TEXT(stored=True),
                    BusinessPhoneNumber = TEXT(stored=True),
                    DocumentURL = TEXT(stored=True),
                    CompleteTextFileURL = TEXT(stored=True),
                    CompleteTextFileSize = TEXT(stored=True),
                    Content = TEXT(stored=True))

    #path = "/Users/Billy/Desktop/rossrc_sec_website/WhooshResults"
    path = "WhooshResults/"
    if not os.path.exists(path):
        os.mkdir(path)        
    ix = whoosh.index.create_in(path, schema)
    ix = whoosh.index.open_dir(path)
    writer = ix.writer()

    # for i in range(0, len(consolidatedIndexID_List)):
    #     writer.add_document(ConslidatedIndexId=str(consolidatedIndexID_List[i]), CompanyName = str(companyName_List[i]), FormType = str(formType_List[i]), CIK = str(cik_List[i]), DateFiled = str(dateFiled_List[i]), URL = str(url_List[i]), Content = str(content_List[i]))
    #     if i % 100 == 0:
    #         print(i)
    for i in range(len(accession_number_list)):
        writer.add_document(AccessionNumber = str(accession_number_list[i]),
                            IRSNumber = str(irs_number_list[i]),
                            CIK = str(cik_list[i]),
                            CompanyName = str(company_name_list[i]),
                            SIC = str(irs_number_list[i]),
                            Industry = str(industry_list[i]),
                            Office = str(office_list[i]),
                            StateOfIncorporation = str(state_of_incorporation_list[i]),
                            FiscalYearEnd = str(fiscal_year_end_list[i]),
                            FormType = str(form_type_list[i]),
                            FilingNumber = str(file_number_list[i]),
                            PeriodOfReport = str(period_of_report_list[i]),
                            FilingDate = str(filing_date_list[i]),
                            AcceptanceDate = str(acceptance_date_list[i]),
                            AcceptanceTime = str(acceptance_time_list[i]),
                            NumberOfDocuments = str(number_of_documents_list[i]),
                            Items = str(items_list[i]),
                            BusinessAddress = str(business_address_list[i]),
                            BusinessPhoneNumber = str(business_phone_number_list[i]),
                            DocumentURL = str(document_url_list[i]),
                            CompleteTextFileURL = str(complete_text_file_url_list[i]),
                            CompleteTextFileSize = str(complete_text_file_size_list[i]),
                            Content = str(scraped_document_list[i]))
        if i % 100 == 0:
            print(i)
    print("At Commiting")
    t1 = time.process_time()
    writer.commit()
    print('It took : ' + str(round(time.process_time() - t1,3)) + ' to commit')

    print('finished once')

    searchtermdownload = ''
    ##################################################

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/exhibits")
    def sec_exhibits():
        statement = '''SELECT datefiled FROM exhibits ORDER BY datefiled DESC LIMIT 1'''
        try:
            conn = psycopg2.connect(database=secret.db_name, user=secret.user_name, host=secret.host, port=secret.port, sslcert=secret.sslcert, sslkey=secret.sslkey, sslrootcert=secret.sslrootcert, sslmode=secret.sslmode)
            cur = conn.cursor()
        except Error as e:
            print(e)

        cur.execute(statement)
        conn.commit()

        date_latest = 'test'

        f = open(VARIABLE_DESCRIPTION_FILE)
        variable_description = json.loads(f.read())
        f.close()
        f = open(DATASET_LIST_FILE)
        dataset_list = json.loads(f.read())
        f.close()

        output_number = random.randint(1,10000000001)
        variable_description_list = variable_description['filings_exibits_variable_description']
        variable_list = dataset_list['filing_exhibits_dataset_list']
        return render_template("exhibits.html", output_number = output_number, variable_description_list=variable_description_list, variable_list = variable_list, date_latest = date_latest)

    ##################################################
    @app.route("/exhibitsoutput", methods=["POST"])
    def exhibitsoutput():
        output_number = request.args.get('output_number', None)

        date_variable = request.form.get('date_variable')
        if date_variable == 'filingdate':
            date_model = 'datefiled'
            open_line = 'SELECT DateFiled, formtype '
        elif date_variable == 'reportdate':
            date_model = 'reportperiod'
            open_line = 'SELECT reportperiod, formtype '

        form_type = request.form.getlist('form_type')
        form_type_str = ""
        for ele in form_type:
            form_type_str += "'"+ele+"', "
        form_type_str_final = "("+form_type_str[:-2]+') '
        #
        startdate = request.form['startdate']
        startdate_split = startdate.split('/')
        startdate_formatted = startdate_split[-1]+'-'+startdate_split[0]+'-'+startdate_split[1]
        enddate = request.form['enddate']
        enddate_split = enddate.split('/')
        enddate_formatted = enddate_split[-1]+'-'+enddate_split[0]+'-'+enddate_split[1]
        date_all = startdate+" - "+enddate
        #
        outputformat = request.form['outputformat']
        #
        companycodeformat = request.form['CompanyCode']
        providecompanycode = request.form['providecompanycode']
        # the value of providecompanycode is decide if the user directly put in the company code, or upload a file, or select the entire database
        CompanyCodeUserPutin = request.form['company_code_user_putin']
        selected = request.form['selected_variable']
        selected_x = selected.split(',')
        variable_dict_check = {'Filing Date':'datefiled', 'Conformed Period of Report or Fiscal Period End':'reportperiod', 'SEC Form':'formtype', 'Company Name':'companyname', 'Reference Name of Complete Report Filing':'filename', 'Complete Report File Size':'filesize', 'SEC Acceptance Date':'secaccdate', 'SEC Acceptance Time':'secacctime', 'Exhibit Sequence Number':'exhibitseq', 'Exhibit Type':'exhibittype', 'Exhibit Description':'exhibitdesc', 'Exhibit Reference Filename':'exhibitfilename'}
        variable_list_str = ""
        for ele in selected_x:
            if ele == 'Filing Date':
                if date_variable == 'filingdate':
                    pass
                elif date_variable == 'reportdate':
                    variable = variable_dict_check[ele]
                    variable_list_str += variable + ','
            elif ele == 'Conformed Period of Report or Fiscal Period End':
                if date_variable == 'filingdate':
                    variable = variable_dict_check[ele]
                    variable_list_str += variable + ','
                elif date_variable == 'reportdate':
                    pass
            elif ele=="SEC Form":
                pass
            else:
                variable = variable_dict_check[ele]
                variable_list_str += variable + ','
        if len(variable_list_str)>0:
            variable_list_str_final = ", "+variable_list_str[:-1] + ' '
        else:
            variable_list_str_final = ''
        #
        if providecompanycode == 'EnterInCompanyCode':

            company_code_list = CompanyCodeUserPutin.split()
            company_code = "( "
            for ele in company_code_list:
                company_code += ele + ", "
            company_code_final = company_code[:-2]+')'
            condition_company_code = 'WHERE ' + companycodeformat + ' in ' + company_code_final
            form_code = ' AND formtype in '+form_type_str_final
        elif providecompanycode == 'SelectEntireDatabase':

            company_code = '*'
            condition_company_code = ''
            form_code = 'WHERE formtype in '+form_type_str_final

        database_name = 'FROM exhibits '

        condition_date_begin2 = ' AND '+date_model+' BETWEEN \''+ startdate_formatted
        condition_date_end2 = '\' AND \'' + enddate_formatted + '\''
        statement = open_line+variable_list_str_final+database_name+condition_company_code+ form_code +condition_date_begin2+condition_date_end2

        try:
            conn = psycopg2.connect(database=secret.db_name, user=secret.user_name, host=secret.host, port=secret.port, sslcert=secret.sslcert, sslkey=secret.sslkey, sslrootcert=secret.sslrootcert, sslmode=secret.sslmode)
            cur = conn.cursor()
        except Error as e:
            print(e)
        # #
        cur.execute(statement)
        conn.commit()

        if outputformat == 'csv':
            output_file_name = "output_"+str(output_number)+".csv"
            output_file_path = "output_file/"

            with open(output_file_path+output_file_name, 'w') as f:
                f = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in cur:
                    f.writerow(row[1:])
        elif outputformat == 'text':
            output_file_name = 'output_'+str(output_number)+'.txt'
            output_file_path = "output_file/"
            with open(output_file_path+output_file_name, 'w') as f:
            # with open('output.txt', 'w') as f:
                for row in cur:
                    f.write(str(row[1:]))

        return render_template("output.html", variable_list=statement, output_file_name = output_file_name,output_number=output_number,date_all=date_all, outputformat=outputformat,selected=selected)
    ##################################################


    @app.route("/eightkoutput", methods=["POST"])
    def eightkoutput():
        output_number = request.args.get('output_number', None)

        # date_variable = request.form['date_variable']
        date_variable = request.form.get('date_variable')

        if date_variable == 'filingdate':
            date_model = 'datefiled'
            open_line = 'SELECT ItemSeqNo, DateFiled '
        elif date_variable == 'reportdate':
            date_model = 'reportperiod'
            open_line = 'SELECT ItemSeqNo, reportperiod '

        startdate = request.form['startdate']
        startdate_split = startdate.split('/')
        startdate_formatted = startdate_split[-1]+'-'+startdate_split[0]+'-'+startdate_split[1]
        enddate = request.form['enddate']
        enddate_split = enddate.split('/')
        enddate_formatted = enddate_split[-1]+'-'+enddate_split[0]+'-'+enddate_split[1]
        date_all = startdate+" - "+enddate

        outputformat = request.form['outputformat']

        companycodeformat = request.form['CompanyCode']
        providecompanycode = request.form['providecompanycode']
        # the value of providecompanycode is decide if the user directly put in the company code, or upload a file, or select the entire database
        CompanyCodeUserPutin = request.form['company_code_user_putin']
        selected = request.form['selected_variable']
        selected_x = selected.split(',')
        variable_dict_check = {'SEC Central Index Key':'cik', 'Filing Date':'datefiled', 'Conformed Period of Report or Fiscal Period End':'reportperiod', 'SEC Form':'formtype', 'Company Name':'companyname', 'Reference Name of Complete Report Filing':'filename', 'Complete Report File Size':'filesize', 'SEC Acceptance Time':'secacctime', 'Form 8-K Item Number':'itemseqno', 'Form 8-K Item Description':'item'}
        variable_list_str = ""
        # need to check  'Number of 8-K Items' first, if so, add COUNT
        for ele in selected_x:
            if ele == 'Filing Date':
                if date_variable == 'filingdate':
                    pass
                elif date_variable == 'reportdate':
                    variable = variable_dict_check[ele]
                    variable_list_str += variable + ','
            elif ele == 'Conformed Period of Report or Fiscal Period End':
                if date_variable == 'filingdate':
                    variable = variable_dict_check[ele]
                    variable_list_str += variable + ','
                elif date_variable == 'reportdate':
                    pass
            elif ele=="Form 8-K Item Number":
                pass
            else:
                variable = variable_dict_check[ele]
                variable_list_str += variable + ','
        if len(variable_list_str)>0:
            variable_list_str_final = ", "+variable_list_str[:-1] + ' '
        else:
            variable_list_str_final = ' '

        selected_trigger = request.form['selected_trigger_event']
        selected_trigger_x = selected_trigger.split(',')
        selected_trigger_final = []
        for ele in selected_trigger_x:
            cleaned = re.search(r'Section \d', ele)
            selected_trigger_final.append(cleaned[0])

        section_dict_check = {'Section 1':"'1.01', '1.02', '1.03'", 'Section 2':"'2.01','2.02','2.03','2.04','2.05','2.06'", 'Section 3':"'3.01','3.02','3.03'", 'Section 4':"'4.01','4.02'", 'Section 5':"'5.01','5.02','5.03','5.04','5.05','5.06','5.07'", 'Section 6':"'6.01','6.02','6.03','6.04','6.05'", 'Section 7':"'7.01'", 'Section 8':"'8.01'", 'Section 9':"'9.01'"}
        trigger_str = ""
        for ele in selected_trigger_final:
            ele_split = ele.split(' - ')
            section_value = ele_split[0]
            section_selected = section_dict_check[section_value]
            trigger_str += section_selected + ','
        trigger_str_final = "("+trigger_str[:-1] + ') '

        if providecompanycode == 'EnterInCompanyCode':
            # this means user directly put in company code
            company_code_list = CompanyCodeUserPutin.split()
            company_code = "( "
            for ele in company_code_list:
                company_code += ele + ", "
            company_code_final = company_code[:-2]+')'
            condition_company_code = 'WHERE ' + companycodeformat + ' in ' + company_code_final
        elif providecompanycode == 'SelectEntireDatabase':
            # select entire database
            company_code = '*'
            condition_company_code = ''

        database_name = 'FROM eightkitems '
        if providecompanycode == 'EnterInCompanyCode':
            condition_company_code = 'WHERE ' + companycodeformat + ' in ' + company_code_final
            trigger_code = ' AND ItemSeqNo in '+trigger_str_final
        elif providecompanycode == 'SelectEntireDatabase':
            condition_company_code = ''
            trigger_code = 'WHERE ItemSeqNo in '+trigger_str_final

        condition_date_begin2 = ' AND '+date_model+' BETWEEN \''+ startdate_formatted
        condition_date_end2 = '\' AND \'' + enddate_formatted + '\''

        statement = open_line+variable_list_str_final+database_name+condition_company_code+ trigger_code +condition_date_begin2+condition_date_end2

        try:
            conn = psycopg2.connect(database=secret.db_name, user=secret.user_name, host=secret.host, port=secret.port, sslcert=secret.sslcert, sslkey=secret.sslkey, sslrootcert=secret.sslrootcert, sslmode=secret.sslmode)
            cur = conn.cursor()
        except Error as e:
            print(e)
        # #
        cur.execute(statement)
        conn.commit()

        if outputformat == 'csv':
            output_file_name = "output_"+str(output_number)+".csv"
            output_file_path = "output_file/"

            with open(output_file_path+output_file_name, 'w') as f:
                f = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in cur:
                    f.writerow(row[1:])
        elif outputformat == 'text':
            output_file_name = 'output_'+str(output_number)+'.txt'
            output_file_path = "output_file/"
            with open(output_file_path+output_file_name, 'w') as f:
            # with open('output.txt', 'w') as f:
                for row in cur:
                    f.write(str(row[1:]))

        return render_template("output.html", variable_list=statement, output_file_name = output_file_name,output_number=output_number,date_all=date_all, outputformat=outputformat,selected=selected)

    @app.route("/eightkitem")
    def sec_eightkitem():
        statement = '''SELECT datefiled FROM eightkitems ORDER BY datefiled DESC LIMIT 1'''
        try:
            conn = psycopg2.connect(database=secret.db_name, user=secret.user_name, host=secret.host, port=secret.port, sslcert=secret.sslcert, sslkey=secret.sslkey, sslrootcert=secret.sslrootcert, sslmode=secret.sslmode)
            cur = conn.cursor()
        except Error as e:
            print(e)
        # #
        cur.execute(statement)
        conn.commit()

        date_latest = 'test'

        f = open(VARIABLE_DESCRIPTION_FILE)
        variable_description = json.loads(f.read())
        f.close()
        f = open(DATASET_LIST_FILE)
        dataset_list = json.loads(f.read())
        f.close()

        output_number = random.randint(1,10000000001)
        variable_description_list = variable_description['eightk_items_variable_description']
        variable_list = dataset_list['eightk_items_dataset_list']
        return render_template("eightkitem.html", output_number = output_number, variable_description_list=variable_description_list, variable_list = variable_list, date_latest = date_latest)

    @app.route("/secfiling")
    def sec_filing():
        statement = '''SELECT datefiled FROM forms ORDER BY datefiled DESC LIMIT 1'''
        try:
            conn = psycopg2.connect(database=secret.db_name, user=secret.user_name, host=secret.host, port=secret.port, sslcert=secret.sslcert, sslkey=secret.sslkey, sslrootcert=secret.sslrootcert, sslmode=secret.sslmode)
            cur = conn.cursor()
        except Error as e:
            print(e)
        # #
        cur.execute(statement)
        conn.commit()
        date_latest = 'test'

        for row in cur:
            date_latest = row[0]
        

        f = open(VARIABLE_DESCRIPTION_FILE)
        variable_description = json.loads(f.read())
        f.close()
        f = open(DATASET_LIST_FILE)
        dataset_list = json.loads(f.read())
        f.close()

        output_number = random.randint(1,10000000001)

        variable_description_list = variable_description['filings_index_variable_description']
        variable_list = dataset_list['filing_index_dataset_list']
        return render_template("secfiling.html", output_number = output_number, variable_description_list=variable_description_list, variable_list = variable_list, date_latest = date_latest)
    #
    @app.route("/output", methods=["POST"])
    def output():
        output_number = request.args.get('output_number', None)

        startdate = request.form['startdate']
        startdate_split = startdate.split('/')
        startdate_formatted = startdate_split[-1]+'-'+startdate_split[0]+'-'+startdate_split[1]
        enddate = request.form['enddate']
        enddate_split = enddate.split('/')
        enddate_formatted = enddate_split[-1]+'-'+enddate_split[0]+'-'+enddate_split[1]
        date_all = startdate+" - "+enddate

        outputformat = request.form['outputformat']

        companycodeformat = request.form['CompanyCode']
        providecompanycode = request.form['providecompanycode']
        # the value of providecompanycode is decide if the user directly put in the company code, or upload a file, or select the entire database
        CompanyCodeUserPutin = request.form['company_code_user_putin']
        selected = request.form['selected_variable']
        selected_x = selected.split(',')
        variable_dict_check = {'SEC Central Index Key':'cik', 'Filing Date':'datefiled', 'SEC Form':'formtype', 'Company Name':'companyname', 'Reference Name of Complete Report Filing':'filename', 'First SEC Date with Index Record Information':'findexdate', 'Last SEC Date with Index Record Information':'lindexdate', 'Index Source':'source'}
        variable_list_str = ""
        for ele in selected_x:
            variable = variable_dict_check[ele]
            variable_list_str += variable + ','
        variable_list_str_final = variable_list_str[:-1] + ' '

        if providecompanycode == 'EnterInCompanyCode':
            company_code_list = CompanyCodeUserPutin.split()
            company_code = "( "
            for ele in company_code_list:
                company_code += ele + ", "
            company_code_final = company_code[:-2]+')'
            condition_company_code = 'WHERE ' + companycodeformat + ' in ' + company_code_final
            condition_date_begin = ' AND secaccdate BETWEEN \'' + startdate_formatted
            condition_date_end = '\' AND \'' + enddate_formatted + '\''

        elif providecompanycode == 'SelectEntireDatabase':
            company_code_final = ''
            condition_company_code = ''
            condition_date_begin = ' WHERE secaccdate BETWEEN \'' + startdate_formatted
            condition_date_end = '\' AND \'' + enddate_formatted + '\''


        open_line = 'SELECT  '

        database_name = 'FROM forms '

        statement = open_line+variable_list_str_final+database_name+condition_company_code+condition_date_begin+condition_date_end

        try:
            conn = psycopg2.connect(database=secret.db_name, user=secret.user_name, host=secret.host, port=secret.port, sslcert=secret.sslcert, sslkey=secret.sslkey, sslrootcert=secret.sslrootcert, sslmode=secret.sslmode)
            cur = conn.cursor()
        except Error as e:
            print(e)
        # #
        cur.execute(statement)
        conn.commit()


        if outputformat == 'csv':
            output_file_name = "output_"+str(output_number)+".csv"
            output_file_path = "output_file/"

            with open(output_file_path+output_file_name, 'w') as f:
                f = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in cur:
                    f.writerow(row[:])
        elif outputformat == 'text':
            output_file_name = 'output_'+str(output_number)+'.txt'
            output_file_path = "output_file/"
            with open(output_file_path+output_file_name, 'w') as f:
                for row in cur:
                    f.write(str(row[1:]))


        return render_template("output.html", variable_list=statement, output_file_name = output_file_name,output_number=output_number,date_all=date_all, outputformat=outputformat,selected=selected)

    @app.route('/download_output')
    def download_output():

        output_number = request.args.get('output_number', None)
        # outputformat = request.form['outputformat']
        # outputformat = request.args.get('outputformat',None)
        outputformat = request.args.get('outputformat',None)
        if outputformat == 'csv':
            file_path = "output_file/output_"+str(output_number)+".csv"
            file_name = "output_"+str(output_number)+".csv"
        elif outputformat == 'text':
            file_path = "output_file/output_"+str(output_number)+".txt"
            file_name = "output_"+str(output_number)+".txt"

        try:
            return send_file(file_path, as_attachment=True, attachment_filename=file_name)
        except Exception as e:
            return (str(outputformat))
            # return render_template("output_error.html")

    @app.route('/manuals')
    def manuals():
        return render_template("manuals.html")

    @app.route('/secfilingsearch', methods=["GET", "POST"])
    def sec_Filing_Search():
        print("on sec filing search")

        if request.args.get("download") != None:
            print("DOWNLOADING")

            try:
                file_path = "output_file/output_searchterm_"+ str(request.args.get("keyword"))+".csv"
                file_name = "output_searchterm_" + str(request.args.get("keyword")) + ".csv"
                return send_file(file_path, attachment_filename=file_name, as_attachment=True)
            except Exception as e:
                return str(e)

        if not request.args.get("keyword"):
            # return render_template("secFilingSearch.html", resultsList = (), pagination = None)
            return render_template("secFilingSearch.html", resultsList = ())
        resultsList = []
        resultsListMatter = []
        searcher = ix.searcher() 
        print("At searcher")
        with ix.searcher() as searcher:
            form_types = []

            for form_type in ("8-K", "10-K"):
                if request.args.get(form_type):
                    form_types.append(form_type)

            t = time.process_time()
            query = QueryParser("Content", schema=ix.schema).parse(request.args.get("keyword"))
            results = searcher.search(query, limit = None)
            search_time = round(time.process_time() - t,4)
            print('It took : ' + str(search_time) + ' to search ')
            
            results.fragmenter.charlimit = None
            # Allow larger fragments
            results.fragmenter.maxchars = 50
            # Show more context before and after
            results.fragmenter.surround = 100
            #print(results)
            t2 = time.process_time()
            for r in results:
                if form_types and (r["FormType"] not in form_types):
                    #print(r["FormType"])
                    continue
                
                keywords = request.args.get("keyword").split()
                frequency = 0
                for keyword in keywords:
                    frequency += r["Content"].lower().count(keyword.lower())
                highlighted = r.highlights("Content")

                # Incase someone tries to use 15 different booleans. Will fail if more than 15 boolean statements are used
                original_highlighted = highlighted.replace('</b>', '</em>').replace('<b class="match term0">', '<em style="background: #ffff99;">').replace('<b class="match term1">', '<em style="background: #ffff99;">').replace('<b class="match term2">', '<em style="background: #ffff99;">').replace('<b class="match term3">', '<em style="background: #ffff99;">').replace('<b class="match term4">', '<em style="background: #ffff99;">').replace('<b class="match term5">', '<em style="background: #ffff99;">').replace('<b class="match term6">', '<em style="background: #ffff99;">').replace('<b class="match term7">', '<em style="background: #ffff99;">').replace('<b class="match term8">', '<em style="background: #ffff99;">').replace('<b class="match term9">', '<em style="background: #ffff99;">').replace('<b class="match term10">', '<em style="background: #ffff99;">').replace('<b class="match term11">', '<em style="background: #ffff99;">').replace('<b class="match term12">', '<em style="background: #ffff99;">').replace('<b class="match term13">', '<em style="background: #ffff99;">').replace('<b class="match term14">', '<em style="background: #ffff99;">').replace('<b class="match term15">', '<em style="background: #ffff99;">')
                

                # resultsList.append((r["ConslidatedIndexId"],r["CompanyName"], r["FormType"], r['CIK'], r['DateFiled'], 'https://www.sec.gov/Archives/' + r['URL'], frequency, highlighted))
                # resultsListMatter.append((r["ConslidatedIndexId"],r["CompanyName"], r["FormType"], r['CIK'], r['DateFiled'], 'https://www.sec.gov/Archives/' + r['URL'], frequency))
                resultsList.append((r["AccessionNumber"],r["IRSNumber"], r['CIK'], r["CompanyName"], r['SIC'], r['Industry'], r['Office'], r['StateOfIncorporation'],
                    r['FiscalYearEnd'], r['FormType'], r['FilingNumber'], r['PeriodOfReport'], r['FilingDate'], r['AcceptanceDate'],
                    r['AcceptanceTime'], r['NumberOfDocuments'], r['Items'], r['BusinessAddress'], r['BusinessPhoneNumber'], r['DocumentURL'],
                    r['CompleteTextFileURL'], r['CompleteTextFileSize'], frequency, original_highlighted))
                resultsListMatter.append((r["AccessionNumber"],r["IRSNumber"], r['CIK'], r["CompanyName"], r['SIC'], r['Industry'], r['Office'], r['StateOfIncorporation'],
                    r['FiscalYearEnd'], r['FormType'], r['FilingNumber'], r['PeriodOfReport'], r['FilingDate'], r['AcceptanceDate'],
                    r['AcceptanceTime'], r['NumberOfDocuments'], r['Items'], r['BusinessAddress'], r['BusinessPhoneNumber'], r['DocumentURL'],
                    r['CompleteTextFileURL'], r['CompleteTextFileSize'], frequency))

                #print('-------------------------------------------------------------------------------------------------------------------------------------------------------')
                #print("Conslidated Index ID :", r["ConslidatedIndexId"])
                #print("Date Filed : ", r["DateFiled"])
                #print(resultsList)
            display_time = round(time.process_time() - t2,3)
            print('It took : ' + str(display_time) + ' to display results for : ' + str(request.args.get("keyword")) + ' with ' + str(len(resultsList)) + ' results')
        
        
       # page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

        # page, per_page, offset = get_page_args(page_parameter = 'page', per_page_parameter = 'per_page')
        total = len(resultsList)
        # pagination_results = get_results(resultsList, offset=offset, per_page=per_page)
        # pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

        searchtermdownload = request.args.get("keyword")
        # Creating Empty Data Frame to use for Downloading CSV File of Results
        if len(resultsListMatter) != 0:
            df_results = pd.DataFrame(resultsListMatter)
            # df_results.to_csv("output_file/output_searchterm_"+ str(request.args.get("keyword"))+ ".csv", index=False, header = ("Consolidated Index ID", "Company Name", "Form Type", "CIK", "Date Filed", "URL", f"Frequency of {searchtermdownload}"))
            df_results.to_csv("output_file/output_searchterm_"+ str(request.args.get("keyword"))+ ".csv", index=False, header = ("Accession Number", "IRS Number", "CIK", "Company Name",	
                                                                                                                                "SIC", "Industry", "Office", "State of Incorporation",
                                                                                                                                "Fiscal Year End", "Form Type", "Filing Number", "Period of Report", 
                                                                                                                                "Filing Date", "Acceptance Date",
                                                                                                                                "Acceptance Time", "Number of Documents Submitted",
                                                                                                                                "Items", "Business Address", "Business Phone Number",
                                                                                                                                "SEC EDGAR URL", "Complete Text File URL", "Text File Size", 
                                                                                                                                f'Frequency of "{searchtermdownload}"'))



        return render_template("secFilingSearch.html", 
                                resultsList = resultsList, 
                                keyword = request.args.get("keyword"), 
                                searchTime = search_time, 
                                displayTime = display_time,
                                # page=page,
                                # per_page=per_page,
                                # results_pagination = pagination_results,
                                # pagination = pagination,
                                eightk = request.args.get("8-K"),
                                tenk = request.args.get("10-K"),)


    """
    for i in ("copy", "test"):
        app.route("/%s" % i)(lambda: render_template("%s.html" % i))
    """
    """
    @app.route('/copy')
    def copy():
        return render_template("copy.html")
        
    @app.route('/test')
    def test():
        return render_template("test.html")
    """

    @app.route('/codelookup', methods=["GET", "POST"])
    def search(): #figre out why changing "search()" to something else crashes everything but filing exhibits on home page
        if request.method == 'POST':
            keyword = request.form['keyword']
            search_condition = request.form.get("search_condition")
            if keyword:
                if search_condition == '1':
                    statement = "SELECT DISTINCT companyname, cik FROM consolidatedindex WHERE consolidatedindex.companyname ILIKE '"+keyword+"%'"
                elif search_condition =='2':
                    statement = "SELECT DISTINCT companyname, cik FROM consolidatedindex WHERE consolidatedindex.companyname ILIKE '%"+keyword+"%'"
                elif search_condition =='3':
                    statement = "SELECT DISTINCT companyname, cik FROM consolidatedindex WHERE consolidatedindex.companyname ILIKE '"+keyword+"'"

                try:
                    conn = psycopg2.connect(database=secret.db_name, user=secret.user_name, host=secret.host, port=secret.port, sslcert=secret.sslcert, sslkey=secret.sslkey, sslrootcert=secret.sslrootcert, sslmode=secret.sslmode)
                    cur = conn.cursor()
                except Error as e:
                    print(e)

                cur.execute(statement)
                conn.commit()

                company_name_cik = {"content":[]}
                for row in cur:
                    dict = {}
                    dict['company_name'] = row[0]             
                    dict['cik'] = row[1]
                    company_name_cik['content'].append(dict)

            else:
                company_name_cik = {"content":[]}

        elif request.method == 'GET':
            company_name_cik = {"content":[]}

        return render_template("codelookup.html", company_name_cik=company_name_cik)


#if __name__=="__main__":
    # init()
    ################# STEP SIX: populate the database at 1 a.m. everyday #################

    # schedule.every().day.at("01:00").do(execute_all)
    #
    # while True:
    #     schedule.run_pending()d
    #     time.sleep(30)
    #app.run(host='0.0.0.0', port=5000,debug=True, use_reloader=False)
app.run(port=5000, debug=True)
