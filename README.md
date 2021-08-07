# surfs_up

## Project Overview
- To perform weather analysis using the provided SQLite database to determine if a surf and ice cream shop is a sustainable business year-round.
## Resources
- Data Sources: 
	- hawaii.sqlite
- Software: 
	- Python 3.8.8
	- Visual Studio Code 1.57.1
	- SQLAchchemy
## Results
- The difference in the average temperature for June and December is 4 degrees Fahrenheit.
- The minimum temperature for December is quite a bit cooler than June, as expected.
- The variation in maximum temperature is only 2 degrees Fahrenheit.
	- June Temperatures:
	    
	    ![June Temps](https://github.com/jediracer/surfs_up/blob/main/images/June%20Temperatures.png)
        - December Temperatures:
        
	    ![December Temps](https://github.com/jediracer/surfs_up/blob/main/images/December%20Temperatures.png)

## Summary
- As expected, the low temperatures in December as lower than June.  However, based on the minimal difference between the average and maximum temperatures, I believe an ice cream and surf shop would do well all year-round.
- To supplement the temperature data I would us the two queies below to collect and summarize the preciptation for June and December.
	```# Supplemental Query for June precipitation
	get_june_precip = session.query(Measurement.prcp).filter(extract('month', Measurement.date)==6).all()
	june_precip = list(np.ravel(get_june_precip))
	june_precip_df = pd.DataFrame(june_precip,columns=['June_Precipitation'])
	june_precip_df.describe()
	
	# Supplemental Query for December precipitation
	get_Decemeber_precip = session.query(Measurement.prcp).filter(extract('month', Measurement.date)==12).all()
	Decemeber_precip = list(np.ravel(get_Decemeber_precip))
	Decemeber_precip_df = pd.DataFrame(Decemeber_precip,columns=['Decemeber_Precipitation'])
	Decemeber_precip_df.describe()
	```