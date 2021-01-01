require "option_parser"

version = 1.2
MAKEOPTS = "-j#{System.cpu_count}"

OptionParser.parse do |parser|
    parser.banner = "gpkg - simple git package installation tool"

    parser.on "-v", "--version", "Prints version information" do
        puts "gpkg version #{version}"
        exit
    end
    parser.on "-h", "--help", "Print the help page" do
        puts parser
        exit
    end
    parser.missing_option do |option_flag|
        STDERR.puts "ERROR: #{option_flag} is missing something."
        STDERR.puts ""
        STDERR.puts parser
        exit(1)
    end
    parser.invalid_option do |option_flag|
        STDERR.puts "ERROR: #{option_flag} is not a valid option."
        STDERR.puts parser
        exit(1)
    end

end

def pkgClone(url : String)
    system "git clone --depth 1 #{url}"
end
