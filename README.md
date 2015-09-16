# CS4501Fall2015

UriDE will be a platform for people (initially college students) to post when and where they’re planning on driving to, and find others who want to go to roughly the same location. This allows them to carpool, saving fuel and money, as well as providing a means of transport to those who may not have one. Systems exist to solve this problem, but they tend to be poorly structured and far from easy to use. Many are simply Facebook groups, relying on postings with no easy way to search, filter, or communicate. Our platform will aim to make finding a ride or advertising a ride far easier, help answer logistical questions that might otherwise be overlooked, and provide payment options if the individuals involved in the transaction would prefer to handle it through our service.
The following is a set of user stories that will guide the initial development of the application:
As a driver, I want to post the details of my travel
     Rough city or town destination, time leaving, willingness to go beyond exact dest, trunk space
As a driver, I want to accept riders in exchange for money
As a driver, I want to define when I get money and what method I use
As a driver, I want to be able to report "bad" riders
As a rider, I want to view postings by destination
     Search by place with range beyond dest
As a rider, I want to be able to make a bid for a ride
     View other bids?
As a rider, I want to be able to view details of the ride
     Where it would be, when it leaves, what they want, type of car, music/ac, priceish
As a rider, I want to be able to view and leave reviews of drivers
     Figure out who is sketch and avoid them
As a user, I want to make a profile
As a user, I want to link my account to Paypal
As a user, I want to be able to delete my account

The following are the basic models we imagine needing as we develop the system:

Users-
	GUID -> Unique, required
	First Name, Last Name-> required, string
	Email-> required, string
	Password-> required, string
	Address-> required, at least a city, string
	Phone number-> required, string
	Payment type-> int id
	payment string-> string like a cc# or paypal account
	transaction history --> List of Ride Type
	gender-> boolean
	driver's license number-> string
	age-> int
	university-> string 
	ratings/reviews-> string/int pairs
	vehicle --> Vehicle type
	
Vehicle-
	GUID-> Unique, required
	max seats-> int
	trunk space-> float
	notes-> string
	mileage/condition-> string
	make-> string
	model-> string
	year-> int
	color-> string
	license plate-> string
	uninsured-> boolean
	AAA/OnStar/Other-> string
	Pets/Handicapped/Babies-> booleans
	
Rides-
	GUID-> required, unique
	Vehicle --> vehicle type
	time to leave-> datetime
	time to arrive-> datetime
	destination-> string
	start location-> string
	Driver --> User type
	riders/luggage --> list of User type, list of floats
	cost structure (levels of price to people)-> list of int pairs
	planned stops (food or rider drop off)-> list of strings
	comments-> string
	maximum distance to drive outside route or destination -> int
	active -> boolean

Service layer
create user
set user inactive 
update user
getUser->by email, name, phone number, university, guid
create ride
update ride
set ride inactive
getRide->source, destination, time leave, time arrive, guid, max distance, riders listed
