# Copyright 2018 ICON Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def upper_snake_to_lower_camel(upper_snake: str) -> str:
    str_array = upper_snake.split('_')
    return str_array[0].swapcase() + ''.join(sub.title() for sub in str_array[1:])


def upper_camel_to_lower_camel(upper_camel: str) -> str:
    return upper_camel[0].lower() + upper_camel[1:]


def convert_method_to_lower_camel(method_name: str) -> str:
    prefix = method_name.split('_')[0]
    method = upper_camel_to_lower_camel(method_name.split('_')[1])
    return prefix + '_' + method
