package main

import (
	"fmt"
	"time"
	"sync"
)

const conferenceTickets int = 50            //constant cannot be changed and data type can be mentioned but not necessary
var conferenceName = "Go Conference"        // in this type you cannot declare constants
var remainingTickets uint = 50              //variable can be changed
var bookings = make([]UserData, 0) // define slice of maps

// create a struct
type UserData struct {
	firstName string
	lastName string
	email string
	numberOfTickets uint
}

var wg = sync.WaitGroup{}

func main() {

	greetUsers()
	// print data types of variables
	fmt.Printf("conferenceTickets is %T, remainingTickets is %T, conferenceName is %T\n", conferenceTickets, remainingTickets, conferenceName)

	//for { // loop until all tickets are booked or no more tickets are available
		firstName, lastName, email, userTickets := getUserInput()
		isValidName, isValidEmail, isValidTickets := validateUserInput(firstName, lastName, email, userTickets)

		if isValidName && isValidEmail && isValidTickets {
			
			bookTicket(userTickets, firstName, lastName, email)
			
			wg.Add(1)
			go sendTickets(userTickets, firstName, lastName, email)
			
			// fmt.Printf("The whole slice: %v\n", bookings)
			// fmt.Printf("The first value: %v\n", bookings[0])
			// fmt.Printf("slice type: %T\n", bookings)
			// fmt.Printf("slice length: %v\n", len(bookings))
			bookTicket(userTickets, firstName, lastName, email)
			firstNames := getFirstNames()
			fmt.Printf("These firstnames of total bookings in our app: %v\n", firstNames)

			noTicketsRemaining := remainingTickets == 0 // alternatively, var noTicketsRemaining bool = remainingTickets == 0
			if noTicketsRemaining {
				// end program
				fmt.Println("Our conference is booked out.")
				// break
			}
		} else {
			if !isValidName {
				fmt.Println("Firstname and lastname must be at least 2 characters long.")
			}
			if !isValidEmail {
				fmt.Println("Email address is invalid.")
			}
			if !isValidTickets {
				fmt.Println("Number of tickets must be greater than 0 and less than or equal to remaining tickets.")
			}
		}
	//}
	wg.Wait()
}

func greetUsers() {
	fmt.Printf("Welcome to %v booking application\n", conferenceName)
	fmt.Printf("We have total of %v tickets and %v are still available.\n", conferenceTickets, remainingTickets)
	fmt.Println("Get your tickets here to attend")
}

func getFirstNames() []string {
	firstNames := []string{} // define slice of strings
	for _, booking := range bookings {
		firstNames = append(firstNames, booking.firstName)
	}
	return firstNames
}

func getUserInput() (string, string, string, uint) {
	var firstName string
	var lastName string
	var email string
	var userTickets uint

	// ask for input
	fmt.Println("Enter your first name: ")
	fmt.Scan(&firstName) // scans user input and assigns it to the variable

	fmt.Println("Enter your surname: ")
	fmt.Scan(&lastName)

	fmt.Println("Enter your email address: ")
	fmt.Scan(&email)

	fmt.Println("Enter your number of tickets: ")
	fmt.Scan(&userTickets)
	return firstName, lastName, email, userTickets
}

func bookTicket(userTickets uint, firstName string, lastName string, email string) {
	remainingTickets = remainingTickets - userTickets
	// create a map for a user
	var userData = UserData {
		firstName: firstName,
		lastName: lastName,
		email: email,
		numberOfTickets: userTickets,
	}

	// append the user to the slice
	bookings = append(bookings, userData)          // append user data to slice
	fmt.Printf("List of bookings: %v\n", bookings) // print slice of maps

	fmt.Printf("Thanks %v %v for booking %v tickets. You will receive confirmation at %v\n", firstName, lastName, userTickets, email)
	fmt.Printf("%v tickets remaining for %v\n", remainingTickets, conferenceName)
}

func sendTickets(userTickets uint, firstName string, lastName string, email string) {
	time.Sleep(10 * time.Second)
	var ticket = fmt.Sprintf("%v tickets for %v %v", userTickets, firstName, lastName)
	fmt.Println("#############################################")
	fmt.Printf("Sending ticket:\n %v \nto email address %v\n", ticket, email)
	fmt.Println("#############################################")
	wg.Done()
}
