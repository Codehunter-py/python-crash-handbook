package main

import "strings"

func validateUserInput(firstname string, lastname string, email string, userTickets uint) (bool, bool, bool) {
	// check valid user input
	isValidName := len(firstname) >= 2 && len(lastname) >= 2
	isValidEmail := strings.Contains(email, "@") && strings.Contains(email, ".")
	isValidTickets := userTickets > 0 && userTickets <= remainingTickets
	return isValidName, isValidEmail, isValidTickets
}
