#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-slim
Version  : 3.0.7
Release  : 11
URL      : https://rubygems.org/downloads/slim-3.0.7.gem
Source0  : https://rubygems.org/downloads/slim-3.0.7.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-slim-bin
BuildRequires : ruby
BuildRequires : rubygem-asciidoctor
BuildRequires : rubygem-builder
BuildRequires : rubygem-creole
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-redcarpet
BuildRequires : rubygem-sass
BuildRequires : rubygem-temple
BuildRequires : rubygem-tilt

%description
# Slim
[![Gem Version](https://img.shields.io/gem/v/slim.svg)](http://rubygems.org/gems/slim) [![Build Status](https://img.shields.io/travis/slim-template/slim.svg?branch=master)](http://travis-ci.org/slim-template/slim) [![Dependency Status](https://img.shields.io/gemnasium/slim-template/slim.svg?travis)](https://gemnasium.com/slim-template/slim) [![Code Climate](https://codeclimate.com/github/slim-template/slim/badges/gpa.svg)](https://codeclimate.com/github/slim-template/slim) [![Test Coverage](https://codeclimate.com/github/slim-template/slim/badges/coverage.svg)](https://codeclimate.com/github/slim-template/slim/coverage) [![Gittip donate button](https://img.shields.io/gratipay/bevry.svg)](https://www.gittip.com/min4d/ "Donate weekly to this project using Gittip")
[![Flattr donate button](https://raw.github.com/balupton/flattr-buttons/master/badge-89x18.gif)](https://flattr.com/submit/auto?user_id=min4d&url=http%3A%2F%2Fslim-lang.org%2F "Donate monthly to this project using Flattr")

%package bin
Summary: bin components for the rubygem-slim package.
Group: Binaries

%description bin
bin components for the rubygem-slim package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n slim-3.0.7
gem spec %{SOURCE0} -l --ruby > rubygem-slim.gemspec

%build
export LANG=C
gem build rubygem-slim.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
slim-3.0.7.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/slim-3.0.6 && rake --trace test && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/slim-3.0.7.gem
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/CHANGES
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/README.jp.md
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/README.md
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/benchmarks/context.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/benchmarks/profile-parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/benchmarks/profile-render.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/benchmarks/run-benchmarks.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/benchmarks/run-diffbench.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/benchmarks/view.erb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/benchmarks/view.haml
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/benchmarks/view.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/bin/slimrb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/doc/include.md
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/doc/jp/include.md
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/doc/jp/logic_less.md
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/doc/jp/smart.md
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/doc/jp/translator.md
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/doc/logic_less.md
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/doc/smart.md
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/doc/translator.md
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/code_attributes.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/command.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/controls.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/do_inserter.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/embedded.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/end_inserter.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/engine.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/erb_converter.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/grammar.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/include.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/interpolation.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/logic_less.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/logic_less/context.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/logic_less/filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/smart.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/smart/escaper.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/smart/filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/smart/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/splat/builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/splat/filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/template.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/translator.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/lib/slim/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/slim.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_code_blocks.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_code_escaping.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_code_evaluation.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_code_output.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_code_structure.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_commands.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_embedded_engines.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_encoding.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_erb_converter.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_html_attributes.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_html_escaping.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_html_structure.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_parser_errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_pretty.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_ruby_errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_slim_template.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_tabs.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_text_interpolation.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_thread_options.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/core/test_unicode.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/include/files/recursive.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/include/files/slimfile.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/include/files/subdir/test.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/include/files/textfile
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/include/test_include.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/literate/TESTS.md
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/literate/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/literate/run.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/logic_less/test_logic_less.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/controllers/application_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/controllers/entries_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/controllers/slim_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/helpers/application_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/models/entry.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/entries/edit.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/layouts/application.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/_partial.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/content_for.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/erb.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/form_for.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/helper.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/integers.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/no_layout.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/normal.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/partial.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/splat.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/thread_options.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/variables.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/app/views/slim/xml.slim
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config.ru
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config/application.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config/boot.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config/environment.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config/environments/test.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config/initializers/backtrace_silencers.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config/initializers/inflections.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config/initializers/mime_types.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config/initializers/secret_token.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config/initializers/session_store.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config/locales/en.yml
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/config/routes.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/script/rails
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/rails/test/test_slim.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/smart/test_smart_text.rb
/usr/lib64/ruby/gems/2.3.0/gems/slim-3.0.7/test/translator/test_translator.rb
/usr/lib64/ruby/gems/2.3.0/specifications/slim-3.0.7.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/slimrb
