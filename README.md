# Screenshot_try

## Modules

- Creating the new file handler to capture when new image is added to the folder
- Creating Image processor workflow which extracts the content from the image
- Classification module **Does it need any furthur processing** like for error need to find the fix or give some suggestions
- Vectordb to store the processed image and suggestions
- Reterival for the user query

## Listner Module

Let us start by understand how to create a listner which listens to a folder and if a image is created in that folder, it captures the event which can be used furthur

There are two ways of doing so
- Polling
- OS events 

### Polling
It is a while loop which is always running to listed the changes in the folder. This is not a efficient way since it takes the CPU usage when it is running...

### OS Event
The packages like watchdog helps... when there is a change in the folder there is an interrupt which can be used to trigger our function which can be used whcih is considered as the efficient method


