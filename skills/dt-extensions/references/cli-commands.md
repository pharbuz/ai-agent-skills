# dt-sdk CLI Commands

Source: https://dynatrace-extensions.github.io/dt-extensions-python-sdk/

## Create
```
$ dt-sdk create --help
                                                                                
 Usage: dt-sdk create [OPTIONS] EXTENSION_NAME                                  
                                                                                
 Creates a new python extension                                                 
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    extension_name      TEXT  [required]                                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --output  -o      PATH                                                       │
│ --help                  Show this message and exit.                          │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Build
```
$ dt-sdk build --help
                                                                                
 Usage: dt-sdk build [OPTIONS] [EXTENSION_DIR]                                  
                                                                                
 Runs wheel, assemble and sign. Downloads dependencies, creates and signs the   
 extension zip file                                                             
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   extension_dir      [EXTENSION_DIR]  Path to the python extension           │
│                                       [default: .]                           │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --private-key           -k      PATH  Path to the dev fused key-certificate  │
│                                       [default:                              │
│                                       /home/runner/.dynatrace/certificates/… │
│ --target-directory      -t      PATH                                         │
│ --extra-platform        -e      TEXT  Download wheels for an extra platform  │
│ --extra-index-url       -i      TEXT  Extra index url to use when            │
│                                       downloading dependencies               │
│ --find-links            -f      TEXT  Extra index url to use when            │
│                                       downloading dependencies               │
│ --only-extra-platforms  -o            Only build for the extra platforms,    │
│                                       useful when building from arm64 (mac)  │
│ --python-version        -p      TEXT  Python versions to download wheels     │
│                                       for. Supported: 3.10, 3.14             │
│ --no-index                            Pass --no-index to pip, ignoring the   │
│                                       package index (only --find-links       │
│                                       sources will be used)                  │
│ --help                                Show this message and exit.            │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Run
```
$ dt-sdk run --help
                                                                                
 Usage: dt-sdk run [OPTIONS] [EXTENSION_DIR]                                    
                                                                                
 Runs an extension, this is used during development to locally run and test an  
 extension                                                                      
                                                                                
 :param extension_dir: The directory of the extension, by default this is the   
 current directory                                                              
 :param activation_config: The activation config file, by default this is       
 activation.json                                                                
 :param secrets: The secrets file to be used to enrich the activation config,   
 by default this is secrets.json                                                
 :param fast_check: If true, run a fastcheck and exits                          
 :param local_ingest: If true, send metrics to localhost:14499 on top of        
 printing them                                                                  
 :param local_ingest_port: The port to send metrics to, by default this is      
 14499                                                                          
 :param print_metrics: If true, print metrics to the console                    
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   extension_dir      [EXTENSION_DIR]  [default: .]                           │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --activation-config                          TEXT     [default:              │
│                                                       activation.json]       │
│ --secrets                                    TEXT     [default:              │
│                                                       secrets.json]          │
│ --fastcheck                                                                  │
│ --local-ingest                                                               │
│ --local-ingest-port                          INTEGER  [default: 14499]       │
│ --print-metrics        --no-print-metrics             [default:              │
│                                                       print-metrics]         │
│ --help                                                Show this message and  │
│                                                       exit.                  │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Upload
```
$ dt-sdk upload --help
                                                                                
 Usage: dt-sdk upload [OPTIONS] [EXTENSION_PATH]                                
                                                                                
 Upload the extension to a Dynatrace environment                                
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   extension_path      [EXTENSION_PATH]  Path to the extension folder or      │
│                                         built zip file                       │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --tenant-url  -u      TEXT  Dynatrace tenant URL                             │
│ --api-token   -t      TEXT  Dynatrace API token                              │
│ --validate    -v            Validate only                                    │
│ --help                      Show this message and exit.                      │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Help
```
$ dt-sdk --help
                                                                                
 Usage: dt-sdk [OPTIONS] COMMAND [ARGS]...                                      
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ run        Runs an extension, this is used during development to locally run │
│            and test an extension                                             │
│ build      Runs wheel, assemble and sign. Downloads dependencies, creates    │
│            and signs the extension zip file                                  │
│ assemble   Creates the extension zip file, without signing it yet            │
│ wheel      Downloads the dependencies of the extension to the lib folder     │
│ sign       Signs the extension zip file using the provided fused             │
│            key-certificate                                                   │
│ upload     Upload the extension to a Dynatrace environment                   │
│ gencerts   Generate root and developer certificates and key                  │
│ create     Creates a new python extension                                    │
│ format     Runs ruff format on the extension code                            │
│ lint       Runs ruff check on the extension code                             │
│ ruff-init  Adds ruff rules if they don't exist already                       │
│ version    Version commands                                                  │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Assemble
```
$ dt-sdk assemble --help
                                                                                
 Usage: dt-sdk assemble [OPTIONS] [EXTENSION_DIR]                               
                                                                                
 Creates the extension zip file, without signing it yet                         
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   extension_dir      [EXTENSION_DIR]  Path to the python extension           │
│                                       [default: .]                           │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --output  -o      PATH                                                       │
│ --force   -f            Force overwriting the output zip file                │
│                         [default: True]                                      │
│ --help                  Show this message and exit.                          │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Generate Certificates
```
$ dt-sdk gencerts --help
                                                                                
 Usage: dt-sdk gencerts [OPTIONS]                                               
                                                                                
 Generate root and developer certificates and key                               
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --output  -o      PATH  Path to the output directory                         │
│                         [default: /home/runner/.dynatrace/certificates]      │
│ --force   -f            Force overwriting the certificates                   │
│ --help                  Show this message and exit.                          │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Sign
```
$ dt-sdk sign --help
                                                                                
 Usage: dt-sdk sign [OPTIONS] [ZIP_FILE]                                        
                                                                                
 Signs the extension zip file using the provided fused key-certificate          
                                                                                
 :param zip_file: The path to the extension zip file to sign                    
 :param certificate: The developer fused key-certificate to use for signing     
 :param output: The path to the output zip file, if not specified, we put it in 
 the dist folder                                                                
 :param force: If true, overwrite the output zip file if it exists              
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   zip_file      [ZIP_FILE]  Path to the extension zip file                   │
│                             [default: dist/extension.zip]                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --certificate  -c      PATH  Path to the dev fused key-certificate           │
│                              [default:                                       │
│                              /home/runner/.dynatrace/certificates/developer… │
│ --output       -o      PATH                                                  │
│ --force        -f            Force overwriting the output zip file           │
│                              [default: True]                                 │
│ --help                       Show this message and exit.                     │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Wheel
```
$ dt-sdk wheel --help
                                                                                
 Usage: dt-sdk wheel [OPTIONS] [EXTENSION_DIR]                                  
                                                                                
 Downloads the dependencies of the extension to the lib folder                  
                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│   extension_dir      [EXTENSION_DIR]  Path to the python extension           │
│                                       [default: .]                           │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --extra-platform        -e      TEXT  Download wheels for an extra platform  │
│ --extra-index-url       -i      TEXT  Extra index url to use when            │
│                                       downloading dependencies               │
│ --find-links            -f      TEXT  Extra index url to use when            │
│                                       downloading dependencies               │
│ --only-extra-platforms  -o            Only build for the extra platforms,    │
│                                       useful when building from arm64 (mac)  │
│ --python-version        -p      TEXT  Python versions to download wheels     │
│                                       for. Supported: 3.10, 3.14             │
│ --no-index                            Pass --no-index to pip, ignoring the   │
│                                       package index (only --find-links       │
│                                       sources will be used)                  │
│ --help                                Show this message and exit.            │
╰──────────────────────────────────────────────────────────────────────────────╯
```
