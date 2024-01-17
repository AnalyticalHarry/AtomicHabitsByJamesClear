function atomicHabit(days) {
    //compounded improvement
    const betterImprovement = Math.pow(1.01, days);
    
    //compounded decline
    const worseImprovement = Math.pow(0.99, days);
  
    //output results
    console.log("=".repeat(40));
    console.log("Atomic Habit Calculator");
    console.log("=".repeat(40));
    console.log(`\nCompound interest for better self-improvement in ${days} days is ${betterImprovement.toFixed(2)}%`);
    console.log(`\nCompound interest for worse self-improvement in ${days} days is ${worseImprovement.toFixed(2)}%`);
    console.log("=".repeat(40));
  }
//calling function with 365 days
atomicHabit(365); 
  
