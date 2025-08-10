def escape_markdown_characters(content):
    """
    转义Markdown中的特殊字符
    
    Args:
        content (str): 原始文本内容
        
    Returns:
        str: 转义后的文本内容
    """
    # Markdown特殊字符及其转义序列
    escape_chars = {
        '\\': r'\\',    # 反斜杠
        '`': r'\`',     # 反引号
        '*': r'\*',     # 星号
        '_': r'\_',     # 下划线
        '[': r'\[',     # 左方括号
        ']': r'\]',     # 右方括号
        '(': r'\(',     # 左圆括号
        ')': r'\)',     # 右圆括号
        '~': r'\~',     # 波浪线
        '#': r'\#',     # 井号
        '+': r'\+',     # 加号
        '-': r'\-',     # 减号
        '£': r'\£',     # 英镑符号
        '.': r'\.',     # 点号
        '!': r'\!',     # 感叹号
    }
    
    # 注意：反斜杠必须首先处理，避免重复转义
    result = content.replace('\\', r'\\')
    
    # 处理其他字符
    for char, escaped in escape_chars.items():
        if char != '\\':  # 反斜杠已经处理过了
            result = result.replace(char, escaped)
    
    return result


def convert_newlines_to_br(input_file, output_file):
    """
    将txt文件中的换行符替换为<br>标签，并转义Markdown特殊字符
    
    Args:
        input_file (str): 输入文件路径
        output_file (str): 输出文件路径
    """
    try:
        # 读取输入文件
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 对Markdown特殊字符进行转义
        converted_content = escape_markdown_characters(content)
        
        # 将换行符替换为<br>
        converted_content = converted_content.replace('\n', '<br>')
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(converted_content)
        
        print(f"转换完成！")
        print(f"输入文件: {input_file}")
        print(f"输出文件: {output_file}")
        
    except FileNotFoundError:
        print(f"错误：找不到文件 '{input_file}'")
    except Exception as e:
        print(f"发生错误: {e}")


def main():
    # 方式1: 直接指定文件路径
    input_file = "input.txt"  # 修改为你的输入文件路径
    output_file = "output.txt"  # 修改为你的输出文件路径
    
    convert_newlines_to_br(input_file, output_file)
    
    # 方式2: 交互式输入文件路径（取消下面的注释来使用）
    """
    input_file = input("请输入源文件路径: ").strip()
    output_file = input("请输入输出文件路径: ").strip()
    convert_newlines_to_br(input_file, output_file)
    """


# 高级版本：处理不同类型的换行符和转义Markdown特殊字符
def convert_newlines_to_br_advanced(input_file, output_file, preserve_double_newlines=False):
    """
    高级版本：处理不同操作系统的换行符，并转义Markdown特殊字符
    
    Args:
        input_file (str): 输入文件路径
        output_file (str): 输出文件路径
        preserve_double_newlines (bool): 是否保留双换行符为<br><br>
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 首先转义Markdown特殊字符
        content = escape_markdown_characters(content)
        
        # 处理不同操作系统的换行符
        # Windows: \r\n, Unix/Linux: \n, Mac: \r
        if preserve_double_newlines:
            # 先处理双换行符
            content = content.replace('\r\n\r\n', '<br><br>')
            content = content.replace('\n\n', '<br><br>')
            content = content.replace('\r\r', '<br><br>')
            # 再处理单换行符
            content = content.replace('\r\n', '<br>')
            content = content.replace('\n', '<br>')
            content = content.replace('\r', '<br>')
        else:
            # 统一处理所有换行符
            content = content.replace('\r\n', '<br>')
            content = content.replace('\n', '<br>')
            content = content.replace('\r', '<br>')
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"高级转换完成！")
        print(f"输入文件: {input_file}")
        print(f"输出文件: {output_file}")
        
    except FileNotFoundError:
        print(f"错误：找不到文件 '{input_file}'")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    main()
    
    # 如果需要使用高级版本，取消下面的注释
    """
    print("\n--- 高级版本演示 ---")
    convert_newlines_to_br_advanced("input.txt", "output_advanced.txt", preserve_double_newlines=True)
    """