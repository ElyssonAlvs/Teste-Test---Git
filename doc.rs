use std::io;

fn main() {
    loop {
        println!("Digite o primeiro número:");
        let mut num1 = String::new();
        io::stdin().read_line(&mut num1).expect("Falha ao ler a entrada");

        let num1: f64 = match num1.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Entrada inválida. Por favor, tente novamente.");
                continue;
            }
        };

        println!("Digite o segundo número:");
        let mut num2 = String::new();
        io::stdin().read_line(&mut num2).expect("Falha ao ler a entrada");

        let num2: f64 = match num2.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Entrada inválida. Por favor, tente novamente.");
                continue;
            }
        };

        println!("Escolha uma operação:");
        println!("1. Soma");
        println!("2. Subtração");
        println!("3. Multiplicação");
        println!("4. Divisão");

        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Falha ao ler a entrada");

        let choice: u32 = match choice.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Entrada inválida. Por favor, tente novamente.");
                continue;
            }
        };

        let result = match choice {
            1 => num1 + num2,
            2 => num1 - num2,
            3 => num1 * num2,
            4 => num1 / num2,
            _ => {
                println!("Operação inválida. Por favor, tente novamente.");
                continue;
            }
        };

        println!("O resultado é: {}", result);
        break;
    }
}