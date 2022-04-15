package main

import (
   "fmt"
   "strings"
)


func main() {
	conferenceName := "Go Conference" // in this type you cannot declare constants
	const conferenceTickets int = 50 //constant cannot be changed and data type can be mentioned but not necessary
	var remainingTickets uint = 50 //variable can be changed
   var bookings []string
   
   // print data types of variables
   fmt.Printf("conferenceTickets is %T, remainingTickets is %T, conferenceName is %T\n", conferenceName, conferenceTickets, remainingTickets)
   
   fmt.Printf("Welcome to %v booking application\n", conferenceName)
   fmt.Printf("We have total of %v tickets and %v are still available.\n", conferenceTickets, remainingTickets)
   fmt.Println("Get your tickets here to attend")
   
   for {
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
      
      if userTickets > remainingTickets {
         fmt.Printf("We only have %v tickets remaining, you can't book %v tickets\n", remainingTickets, userTickets)
         break
      }

      remainingTickets = remainingTickets - userTickets
      bookings = append(bookings, firstName + " " + lastName)
   
      // fmt.Printf("The whole slice: %v\n", bookings)
      // fmt.Printf("The first value: %v\n", bookings[0])
      // fmt.Printf("slice type: %T\n", bookings)
      // fmt.Printf("slice length: %v\n", len(bookings))
      
      fmt.Printf("thanks %v %v for booking %v tickets. You will receive confirmation at %v\n", firstName, lastName, userTickets, email)
      fmt.Printf("%v tickets remaining for %v\n", remainingTickets, conferenceName)
      

      firstNames := []string{}
      for _, booking := range bookings {
         var names = strings.Fields(booking)
         firstNames = append(firstNames, names[0])
      }
      fmt.Printf("These firstnames of total bookings in our app: %v\n", firstNames)
   
      noTicketsRemaining := remainingTickets == 0 // alternatively, var noTicketsRemaining bool = remainingTickets == 0 
      if noTicketsRemaining {
         // end program 
         fmt.Println("Our conference is booked out.")
         break
      }
   }
} // conditionals 