create or replace package hr.convert_num_to_str is

  -- Author  : CHEZA
  -- Created : 26.05.2020 14:00:00
  -- Purpose : Convert numbers to text in the Russian language
  
  -- Public function and procedure declarations
  function convert_num_to_str(pr_number         number,
                              pr_is_male_gender pls_integer default 1)
    return varchar2 deterministic;

  -- Public function and procedure declarations
  function convert_num_to_str(pr_number         varchar2,
                              pr_is_male_gender pls_integer default 1)
    return varchar2 deterministic;

end convert_num_to_str;
/
create or replace package body hr.convert_num_to_str is

  -- Function and procedure implementations
  function convert_num_to_str(pr_number         number, /* as number: 1199.00 */
                              pr_is_male_gender pls_integer default 1)
    return varchar2 deterministic is

    l_number   number;
    l_res      varchar2(10000) := cast(null as char);
    c_ZERO     constant varchar2(8) := '����';
    l_thousand number;
    l_ground   number;
    l_d1       number;
    l_d2       number;
    l_d3       number;

  begin

    l_number := pr_number;

    if l_number = 0 then
      return c_ZERO;
    end if;

    while l_number > 0
      loop

        l_thousand := coalesce(l_thousand, 0) + 1;
        l_ground   := mod(l_number, 1000);
        l_number      := (l_number - l_ground) / 1000;

      if l_ground > 0 then
        l_d3 := (l_ground - mod(l_ground, 100)) / 100;
        l_d1 := mod(l_ground, 10);
        l_d2 := (l_ground - l_d3 * 100 - l_d1) / 10;
        if l_d2 = 1 then
          l_d1 := 10 + l_d1;
        end if;

       l_res :=
         case l_d3
           when 1 then ' ���'
           when 2 then ' ������'
           when 3 then ' ������'
           when 4 then ' ���������'
           when 5 then ' �������'
           when 6 then ' ��������'
           when 7 then ' �������'
           when 8 then ' ���������'
           when 9 then ' ���������'
           else ''
         end ||
         case l_d2
           when 2 then ' ��������'
           when 3 then ' ��������'
           when 4 then ' �����'
           when 5 then ' ���������'
           when 6 then ' ����������'
           when 7 then ' ���������'
           when 8 then ' �����������'
           when 9 then ' ���������'
           else ''
         end ||
         case l_d1
           when 1 then
             case when l_thousand = 2 or l_thousand = 1 and pr_is_male_gender = 0
               then ' ����'
               else ' ����'
             end
           when 2 then
             case when l_thousand = 2 or l_thousand = 1 and pr_is_male_gender = 0
               then ' ���'
               else ' ���'
             end
           when 3 then ' ���'
           when 4 then ' ������'
           when 5 then ' ����'
           when 6 then ' �����'
           when 7 then ' ����'
           when 8 then ' ������'
           when 9 then ' ������'
           when 10 then ' ������'
           when 11 then ' �����������'
           when 12 then ' ����������'
           when 13 then ' ����������'
           when 14 then ' ������������'
           when 15 then ' ����������'
           when 16 then ' �����������'
           when 17 then ' ����������'
           when 18 then ' ������������'
           when 19 then ' ������������'
           else ''
         end ||
         case l_thousand
           when 2 then ' �����' ||
             case
               when l_d1 = 1
                 then '�'
               when l_d1 in (2, 3, 4)
                 then '�'
               else ''
             end
           when 3 then ' �������'
           when 4 then ' ��������'
           when 5 then ' ��������'
           when 6 then ' ����������'
           when 7 then ' ����������'
           else ''
         end ||
         case
           when l_thousand in (3, 4, 5, 6, 7) then
             case
               when l_d1 = 1 then ''
               when l_d1 in (2, 3, 4) then '�'
               else '��'
             end
           else ''
         end ||
         coalesce(l_res, '');

      end if;

      end loop;

    return trim(l_res);

  exception
    when others then
      return '��������� �������������� ������!';

  end convert_num_to_str;

  function convert_num_to_str(pr_number         varchar2, /* as string: '1199,00' or '1199.00' */
                              pr_is_male_gender pls_integer default 1)
    return varchar2 deterministic is

    l_number         number;
    l_is_male_gender pls_integer := pr_is_male_gender;

  begin

    l_number := to_number(pr_number, regexp_replace(regexp_replace(pr_number, '\d', 9), '\,', 'D'), 'NLS_NUMERIC_CHARACTERS = '',.''');

    return convert_num_to_str(pr_number => l_number, pr_is_male_gender => l_is_male_gender);

  end convert_num_to_str;

end convert_num_to_str;
/
