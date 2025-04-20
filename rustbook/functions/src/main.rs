fn main() {
    let a = factorial(5);
    println!("{a}");
}

fn factorial(x:i64)->i64{
    if x == 0{
        1
    } else{
        x * factorial(x-1)
    }
}
