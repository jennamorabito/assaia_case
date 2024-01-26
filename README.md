# A small case study for Assaia

## Key assumptions/preprocessing
- For "Median turnaround time," "Longest process," and "Interesting finding," those were derived from a filtered dataset only including total time detected at the gate < 1 day. 
- Lacking meta-data, I had to take a guess at what many columns meant. I'm particularly unsure about which columns most correspond to takeoff and landing, as well as some of the sub-processes

## Tech Stack
- Git
- Python
- Streamlit

## What I would do if I had more time
- Better documentation
- Understand the variables better by doing some domain research
- Find interesting time-series analysis to do - maybe there are seasonal patterns, or a change in the number of late flights after a policy change
- Dig into the correlations, play with correlating different variables
- Do some more rigorous statistical analysis; a regression analysis would be a good place to start
- Deploy my app live so people can access it with just a link
- Add filtering and interactivity to the visualizations so people could explore differences by plane type, airline, etc.

### Python version
3.10.11