#[derive(Debug)]
struct Rectangle{
    width: u32,
    height: u32,
}

impl Rectangle{
    fn area(&self)-> u32{
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool{
        self.area() > other.area()
    }

    fn square(size: u32) -> Self{ //Note this is an associated function not a method
        Self{
            width: size,
            height:size,
        }
    }
}

fn main() {
    let scale = 10;
    let rect = Rectangle{
        width: dbg!(20 * scale),
        height: 30,
    };

    let rect2 = Rectangle{
        width: 12,
        height: 11,
    };

    let rect3 = Rectangle{
        width:300,
        height: 20,
    };

    dbg!(&rect);
    println!("Rectangle can hold rectangle 2? => {:#?}", rect.can_hold(&rect2));
    println!("Rectangle can hold rectangle 3? => {:#?}", rect.can_hold(&rect3));
}
