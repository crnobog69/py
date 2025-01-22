require 'fileutils'

def py_to_md_converter(input_dir)
  # Пролазак кроз све датотеке и поддиректоријуме
  Dir.glob("#{input_dir}/**/*").each do |file|
    if File.file?(file) && File.extname(file) == ".py"
      # Читање .py датотеке и прављење .md датотеке
      code_content = File.read(file)
      md_content = "```python\n#{code_content}\n```"

      output_path = File.join(File.dirname(file), File.basename(file, ".py") + ".md")
      File.write(output_path, md_content)

      puts "Конвертован: #{file} -> #{output_path}"
    end
  end
end

# Пример коришћења
def main
  input_directory = "." # Промените у ваш улазни директоријум
  py_to_md_converter(input_directory)
end

main if __FILE__ == $0
