Summary:	Determine and mark up significant differences between latex files
Name:		latexdiff
Version:	0.5
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dante.ctan.org/tex-archive/support/%{name}.zip
# Source0-md5:	70fdec50c25c5807e7ec071b88d4af49
URL:		http://www.ctan.org/tex-archive/support/latexdiff/
Suggests:	texlive-latex-effects
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Latexdiff is a Perl script for visual mark up and revision of
significant differences between two latex files. Various options are
available for visual markup using standard latex packages such as
color . Changes not directly affecting visible text, for example in
formatting commands, are still marked in the latex source. A
rudimentary revision facilility is provided by another Perl script,
latexrevise, which accepts or rejects all changes. Manual editing of
the difference file can be used to override this default behaviour and
accept or reject selected changes only.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
%{__make} install \
	INSTALLPATH=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLMANPATH=$RPM_BUILD_ROOT%{_mandir} \
	INSTALLEXECPATH=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/latex*.1.*
