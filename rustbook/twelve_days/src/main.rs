fn main() {
    let gifts = ["and a patridge in a pear tree", "two turtle doves", "three fresh hen",
                "four culling birds", "five golden rings"];
    let days = ["1st", "2nd", "3rd", "4th", "5th"];

    let mut count = 0;
    while count < 5{
        let d = days[count];
        // let g = gifts[count];
        println!("On the {d} day of christmas, my true love said to me: ");
        let mut gg = count;
        loop{
            let dd = gifts[gg];
            println!("{dd}");
            if gg <= 0{
                break;
            } else{
                gg -= 1;
            }
        }
        print!("\n");
        count += 1;
    }
}
