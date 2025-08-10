def convert_newlines_to_br(input_file, output_file):
    """
    将txt文件中的换行符替换为<br>标签，将*替换为\*
    
    Args:
        input_file (str): 输入文件路径
        output_file (str): 输出文件路径
    """
    try:
        # 读取输入文件
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 将换行符替换为<br>，将*替换为\*
        converted_content = content.replace('\n', '<br>')
        converted_content = converted_content.replace('*', r'\*')
        
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


# 高级版本：处理不同类型的换行符和转义*字符
def convert_newlines_to_br_advanced(input_file, output_file, preserve_double_newlines=False):
    """
    高级版本：处理不同操作系统的换行符，并将*转义为\*
    
    Args:
        input_file (str): 输入文件路径
        output_file (str): 输出文件路径
        preserve_double_newlines (bool): 是否保留双换行符为<br><br>
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 首先转义*字符
        content = content.replace('*', r'\*')
        
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