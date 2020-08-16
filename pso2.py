import discord
import os
import time
import random
import requests
import asyncio
import imgkit

class pso2_sched:

    def __init__(self):
        current_month_schedule_url = ''

    def get_current_schedule(self):

        response = requests.get("https://pso2.com/news/urgent-quests")

        with open("./files/schedule/current.html", "w") as handler:
            handler.write(response.text)

    def read_current_schedule(self):
        
        news_site = open("./files/schedule/current.html", "r")
        link_check = False

        if (news_site == None):
            print("\n--PSO2: Could not obtain website.\n")
            raise Exception('Maintenance or down')
            
        text = news_site.readline()

        while (text is not None):

            if ("news-section all-news emergency-section active" in text):
                link_check = True
            elif (("ShowDetails" in text) and (link_check)):
                link = text.split("ShowDetails(", 1)[1].split(",", 1)[0].split("'")[1]
                self.current_month_schedule_url = 'https://pso2.com/news/urgent-quests/' + link

                with open("./files/schedule/schedule.html", "w", encoding='UTF-8', newline='') as handler:
                    handler.write(requests.get(self.current_month_schedule_url).text)

                break
            
            text = news_site.readline()
        
        news_site.close()

        # System Print
        print("\n--PSO2 ~ Current Schedule Link: " + self.current_month_schedule_url + "\n")

    def read_schedule_table(self):
        
        if (self.current_month_schedule_url == ''):
            return

        schedule_site = open("./files/schedule/schedule.html", "r")

        if (schedule_site == None):
            print("\n--PSO2: Could not obtain schedule.\n")
            raise Exception('Error while obtaining schedule link.')

        text = schedule_site.readline()

        while (text is not None):

            if ("<table" in text):

                # Need to check this line for times and put them in a list, 
                # since they change 

                w1sched = "<table" + text.split("<table")[1].split("</table>")[0] + "</table>"

                with open("./files/schedule/schedimg.html", "w", encoding='UTF-8') as handler:
                    handler.write(w1sched)

                w2sched = "<table" + text.split("<table")[3].split("</table>")[0] + "</table>"

                with open("./files/schedule/schedimg2.html", "w", encoding='UTF-8') as handler:
                    handler.write(w2sched)
                
                break

            text = schedule_site.readline()

        # Week 1
        imgkit.from_file("./files/schedule/schedimg.html", 
            "./files/schedule/schedimg.png", 
            config=imgkit.config(wkhtmltoimage='D:\Docs\Downloads\Random Stuff\wkhtmltopdf\\bin\wkhtmltoimage.exe'))
        
        # Week 2
        imgkit.from_file("./files/schedule/schedimg2.html", 
            "./files/schedule/schedimg2.png", 
            config=imgkit.config(wkhtmltoimage='D:\Docs\Downloads\Random Stuff\wkhtmltopdf\\bin\wkhtmltoimage.exe'))
        
        schedule_site.close()

        
# Se fonte for >18px e texto for 'Week 1' ou 'Week 2'