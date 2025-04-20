fn main() {
    for i in 0..10{
        print!("{},", fibonacci(i));
    }
    print!("\n");
}

fn fibonacci(x:isize)->isize{
    if x == 0{
        1
    } else if x == 1{
        1
    } else{
        fibonacci(x-1) + fibonacci(x-2)
    }
}